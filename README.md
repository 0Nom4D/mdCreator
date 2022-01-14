# mdCreator

mdCreator is a Python project. mdCreator can create a README.md file using basic Python functionalities.
mdCreator is connected to the Tenor API to get Gifs.

## Before continuing

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=0Nom4D_mdCreator&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=0Nom4D_mdCreator) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=0Nom4D_mdCreator&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=0Nom4D_mdCreator) ![GitHub](https://img.shields.io/github/license/0Nom4D/mdCreator?style=flat-square) [![Documentation](https://img.shields.io/badge/Documentation-PDoc3-blue?style=flat-square)](https://0nom4d.github.io/mdCreator/)

This project is under the jurisdiction of the MIT License. Don't do dumb things.

![Alt Text](https://media.tenor.com/images/4dc761d53f5bad9863d64de1e6cd8db4/tenor.gif)

### Prerequisites

To use this project, you'll need Python (Version 3.8):

* [Python Installation](https://www.python.org/downloads/)

Please refer to this link in order to install `requests python 3 module` and `python-dotenv python 3 module`:

* [Python Requests Module Installation](https://pypi.org/project/requests/)
* [Python Python-Dotenv Module Installation](https://pypi.org/project/python-dotenv/)

### Building program

mdCreator is a little Python Script dedicated to help programmers to not spend 4 hours creating a README.md.
Created README.md is perfectly customisable using a .json configuration file.

mdCreator use Tenor GIF Api. To use mdCreator, you will need a Tenor API Key. To get one, you can check
[this](https://github.com/0Nom4D/mdCreator/wiki/API-Key-Registration).

mdCreator works as it follows:

```term
$> mdCreator --pname <Project Name> -l <Project's Main Language>
```

You can have access to every option, you can use ```-h / --help``` option or read the table below.

| Options                   | Action                                            |  Mandatory         |
| ------------------------- |:-------------------------------------------------:|:------------------:|
| -p / --pname Name         | Project Name                                      | &#9745;            |
| -l / --language Language  | Project's Main Language                           | &#9745;            |
| -a / --array              | Create a table in your README.md                  | &#9744;            |
| -g / --gif [Keywords ...] | Add Gifs corresponding to the keywords you give   | &#9744;            |

You can also change the written categories by changing the mdCreator.json configuration file by adding / removing the categories.
Please use the following syntax while adding categories:

```json lines
{
  "student": {
    "authors": {
      "range": 2,
      "title": "My new title",
      "description": "My new description"
    },
  }
}

where
    range is the size of the title to add to the README (1 is the biggest and 3 is the smallest)
```

**For more information about configuration file, please check the [mdCreator wiki](https://github.com/0Nom4D/mdCreator/wiki/Configuration-File)!**

You now have the choice between a student configuration and a new professional configuration. Feel free to edit the 'pro' section inside the mdCreator.json configuration file.

### Coding Style

mdCreator is developed with Python. There's not a real coding style, but I tried being the cleaner possible.

## Authors

* **Arthur Adam** - [0Nom4D](https://github.com/0Nom4D)

## Contributors

[![Alt Text](https://contrib.rocks/image?repo=0Nom4D/mdCreator)](https://github.com/0Nom4D/mdCreator/graphs/contributors)

