# Annotool Adaptive Fractal Analysis

In this project I will try using Adaptive Fractal Analysis as a method for prioritizing paragraphs for annotations of dramatic arcs in works of literature fiction. The Annotation tool is in another repository part of another course. This project is part of Tiralab course.

## Weekly Reports

You can see weekly report [here](/documentaion)

## Getting Started

Download The Great Gatsby from Project Gutenberg by using command:
```
./admin_tools/download-id.sh 64317
```
Notice that the wget script tends to hang-up without closing. The script should have written the book to `static/books/64317.txt.utf-8`. I have been using this book as an example as it has ready made Dramatica analysis available (you do not need to know anything about that).

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

