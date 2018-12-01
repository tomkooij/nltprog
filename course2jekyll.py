"""
Convert stgm UvA course CMS into static Jekyll pages for GitHub pages.

course CMS: https://github.com/uva/course-site
This ruby on rails app requires "CASClient" for authenicating users and seems
unusable without such service.

This can be used to convert "Inleiding programmeren"
(https://github.com/programmeer/cursus) and similar courses into static
markdown that can be hosted on Github pages using Jekyll

Usage:

copy jekyll stuff (github.com/kbroman/simple_site) into /_staticsite/

/_staticsite/assets
/_staticsite/_layouts
/_staticsite/_includes
/_staticsite/_plugins
/_staticsite/Gemfile
/_staticsite/_config.yml

and run:

`python course2jekyll.py` from the course root folder.

"""

import pathlib
import shutil
import os

COURSE_FOLDER = ''
DEST_FOLDER = '_staticsite'
PAGE_HEADER = '---\nlayout: page\n---\n'


def get_course_path():
    return pathlib.Path.cwd() / COURSE_FOLDER

def get_dest_path():
    return pathlib.Path.cwd() / DEST_FOLDER

def fix_foldername(foldername):
    """
    `10 Getaltheorie` -> `getaltheorie`

    """
    return foldername.split()[1].lower()

def process_course(course_path, dest_path):
    """
    Create a subfolder for each page

    /00 Algoritmen/ -> /algoritmen/

    """
    for path in sorted(course_path.glob('*')):
        if path.name == 'info':
            create_root_index(path, dest_path)
            continue
        if path.is_dir() and str(path.name)[0].isdigit():
            name = fix_foldername(path.name)
            page_dest_path = dest_path / name
            print(f'Folder {path} -> {page_dest_path}')
            if not page_dest_path.exists():
                os.mkdir(page_dest_path)
            process_pages(path, page_dest_path)


def process_pages(page_path, dest_path):
    """
    Create a markdown file for each subpage

    /00 Algoritmen/00 Inhoud -> /algoritmen/inhoud.md

    """
    for path in sorted(page_path.glob('*')):
        if path.is_dir():
            name = fix_foldername(path.name) + '.md'
            print(f' * creating markdown page {name}')
            process_subpages(path, dest_path, md_file = name)


def process_subpages(subpage_path, destination_path, md_file = "index.md"):
    """
    Create a single markdown page from a collection of sub-subfolders.

    concat all markdown files to a single page (markdown file) in parent
    folder and move all images (etc) to parent folder

    """
    markdown = ''
    for path in sorted(subpage_path.glob('*')):
        if path.suffix == '.md':
            markdown += open(path, 'r').read()
        elif not path.is_dir():
            #print(f'copy {path} to {destination_path}')
            shutil.copy(path, destination_path)
    with open(destination_path / md_file, "w") as f:
        f.write(PAGE_HEADER + markdown)


def create_root_index(path, dest_path):
    """read info folder and write main index.md"""
    # TODO add header
    process_subpages(path, dest_path)


course_path = get_course_path()
dest_path = get_dest_path()
process_course(course_path, dest_path)
