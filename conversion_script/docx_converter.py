# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:42:07 2021

@author: mathe
"""
#!/usr/bin/python

import pypandoc
import re
import os
import sys
from datetime import date
from datetime import datetime
import json

# Getting main directory as script path

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

parent = "\\".join(dname.split("\\")[:-1])
print(parent)
print(dname)

# Setting directories
docx_in = dname + "/input/blogs"
header_in = dname + "/input/headers"
image_out = parent + "/images/blogs/" + str(date.today()) + "/"
blog_dir = parent + "/_posts/"
glossary_path = dname + "/resources/glossary.json"

header_plain = dname + "/resources/header_plain"

docx = re.compile(".*\.docx")

# Get data from glossary json
with open(glossary_path) as f:
  gloss = json.load(f)
  f.close()

# Check terms against a glossary and create a relevant piece of heading
def find_terms(glossary, blog):
  sidebar_text = "\nsidebar:\n  - title: \"Glossary\"\n  - text: \""
  found_term = False
  for term in glossary["glossary"]:
    results = len(re.findall(term["term"], blog))
    if results > 0:
      found_term = True
      sidebar_text = sidebar_text + "**" + term["term"] + ":** " + term["def"] + "<br><br>"
  sidebar_text = sidebar_text + "\"\n---"
  if found_term == True:
    return sidebar_text
  else:
    return "---"


# Create string from docx formatted text except those in wrong format
def docx_conv(root, name, images_path):
        author = re.findall(r"(^.*?)\.", name)[0]
        extract_img = "--extract-media=" + images_path + author
        path = os.path.abspath(os.path.join(root, name))
        blog = pypandoc.convert_file(path, 'md', extra_args =["--wrap=none", extract_img])
        return blog, author.lower()


# Add a correctly labelled header to the blog
def header_build (header, name, blog, glossary):
     with open(header, encoding = "utf-8") as f:
            head_in = f.read()
            f.close()
     author = re.findall(r"(^.*?)\.", name)[0]
     author = re.sub(r"\d", "", author)
     author_code = "author: " + author.lower() + "\n"
     head_in = re.sub(r"author:.*\r?\n", author_code, head_in)
     # Sub in the submitted glossary - set up so it will just replace with metadata end placer if glossary empty
     head_in = re.sub(r"\n---", glossary, head_in)
     final = head_in + "\n\n" + blog
     title = re.findall("title:.*\"(.*)\"", head_in)

     if len(title) > 0 and title[0] != "":
          title_s = re.sub(r"[\s:/.,]", "-", title[0])[:40]
     else:
          title_s = str(datetime.now().microsecond)[:3]

     return (final, title_s)





for root, dirs, files in os.walk(docx_in, topdown=False):
    for name in files:
        if docx.match(name):
            print(name + " ...format correct")
            blog, author = docx_conv(root,name, image_out)
            header_path = header_in + "/" + author + ".yml"
            glossary = find_terms(gloss, blog)
            if os.path.exists(header_path):
              final, title_s = header_build(header_path, name, blog, glossary)
            else:
              final, title_s = header_build(header_plain, name, blog, glossary)

            # Cleaning out uncessary md and tags from the final piece and converting images so they link to gallery view
            final = re.sub(r"\!\[\]\((.*)(/images/.*)\)", r"[![](\2)](\2)", final)
            final = re.sub(r"{width=.*?}", "", final)



            # Create outpath - check that file doesn't already exist
            outpath = blog_dir + str(date.today()) + "-" + title_s + ".md"
            file_no = 0
            while os.path.isfile(outpath):
                file_no = file_no + 1
                outpath = blog_dir + str(date.today()) + "-" + title_s + str(file_no) + ".md"

            # Write out final blog to correct destination
            f = open(outpath, "w", encoding = "utf-8")
            f.write(final)
            f.close()
            print(outpath + "...written to blog directory")


        else:
            print("error!:\n" + name + " is not correctly formatted. \n Use docx.")
            continue




