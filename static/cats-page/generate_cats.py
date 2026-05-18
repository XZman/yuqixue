#!/usr/bin/env python3

import os
import sys
import glob

cat_file_dir = sys.argv[1]

cat_file_name_list = glob.glob(os.path.join(cat_file_dir, "*.jpg"))

assert len(cat_file_name_list) > 0, cat_file_name_list

template_str = '''<article class="thumb">
    <a href="{%FILENAME}" class="image"><img src="{%FILENAME}" alt="" /></a>
    <!-- <h2>{%TITLE}</h2>
    <p>{%DESCRIPTION}</p> -->
</article>
'''

with open("generated_cats.html", "w") as f:
    for cat in cat_file_name_list:
        cat_str = template_str.replace("{%FILENAME}", cat)
        f.write(cat_str)
