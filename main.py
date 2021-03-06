#!/usr/bin/env python
import click
import shutil
import randomname

#from random import choice

main_dir = "/home/cristian/programs/newp/templates/"

def py_temp(path, name):
    """copy the template to path

    Args:
        path (str): path to create the project
    """
    shutil.copytree(main_dir+"py", path+name)
    #print(path + "/" + name)

def cpp_temp(path, name):
    """copy the template to path

    Args:
        path (str): path to create the project
    """
    shutil.copytree(main_dir+"cpp", path+name)
    #print(path + "/" + name)

def web_temp(path, name):
    """copy the template to path

    Args:
        path (str): path to create the project
    """
    shutil.copytree(main_dir+"web", path+name)
    #print(path + "/" + name)
    
def codename():
    return randomname.get_name(
        noun=(
            "chemistry",
            "gaming",
            "military_navy",
            "web_development",
            "metals",
            "military_airforce",
            "astronomy",
            "minerals",
            "birds",
            )
        )

@click.command()
@click.argument("lang")
@click.argument("path")
@click.option("--name")
def main(lang, path, name):
    if name == None:
        name = codename()
        templates_funcs[lang](path, name)    
    else:
        try:
            templates_funcs[lang](path, name)
            raise "to trying"
        except:
            print("error")

templates_funcs = {
    "py":py_temp,
    "cpp":cpp_temp,
    "web":web_temp,
}

if __name__ == "__main__":
    main()
