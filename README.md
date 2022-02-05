# Annotool Adaptive Fractal Analysis

In this project I will try using Adaptive Fractal Analysis as a method for prioritizing paragraphs for annotations of dramatic arcs in works of literature fiction. The Annotation tool is in another repository part of another course. This project is part of Tiralab course.

## Weekly Reports

You can see weekly report [here](https://github.com/AhtiAhde/AnnotoolAFA/tree/main/documentation)

## Getting Started

Create your choice of virtualenvironment (for example, like the first two lines) and then install the dependencies by running:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then download The Great Gatsby from Project Gutenberg by using command:
```
./admin_tools/download-id.sh 64317
```
Notice that the wget script tends to hang-up without closing. The script should have written the book to `static/books/64317.txt.utf-8`. I have been using this book as an example as it has ready made Dramatica analysis available (you do not need to know anything about that).

### Runing the tests

You can run the unit tests by:
```
python -m pytest tests/
```

### Testing the Data Science aspects

The pip dependencies should have installed `jupyter notebook` for you, so you can just:
```
jupyter notebook
```
And follow the link and then run the notebook in the `notebooks/` directory. Here you have all the well documented experiments and test results I have done so far (for some reason the jupyter might give you `This command cannot be run due to the error: The system cannot find the file specified.`; however, that is a false alarm and the notebooks run fine regardless).

### Testing the UI (optional)

First you need to start your own instance of Postgres database and the import the Postgres database schema by running:
```
pg_dump postgres -O -x > import.psql
```

Then create `.env` file, like:
```
ADMIN_USER=Admin
ADMIN_PASSWORD=123asd123
MASTER_MODE=enabled
```

Then you can start Flask:
```
flask run
```

And start by navigating to the `admin/login`-view. I might change this bit later on as I think this would work better without UI of this sort.
