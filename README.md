# django-include-strip-tag

A new "include_strip" template tag for Django

## Introduction

This new templatetag, `include_strip`, works exactly the same as the default `include` template tag provided by Django.

The only difference is that the `strip` method is applied to the result, to remove leading and trailing spaces.

The aim is to remove the unwanted space added in text when including a template that just return some text.


## Installation

`django-include-strip-tag` is available on Pypi:

```
pip install django-include-strip-tag
```

Or you can find it on github: https://github.com/twidi/django-include-strip-tag

When installed, just add `include_strip_tag` to your `INSTALLED_APPS` in the `settings.py` file of your django project.


## Usage

Simply add the tags library in your template, and use `include_strip` instead of `include` when needed:

```django
{% load include_strip %}
Hello {% include_strip "user.html %}, how are you today ?
```

## Why ?

Considering the "user.html" template:

```django
SomeUserName
```

In the previous template (in "Usage"), without this new templatetag, the result would be:

```
Hello SomeUSerName , how are you today ?
```

With `include_strip`, we have:

```
Hello SomeUSerName, how are you today ?
```

Notice the difference between the username and the coma... It's because the newline at the end of the included template is kept when the result is added to the parent template.

So the `include_strip` apply the `strip` method (on the result, which is a string) to remove it.

It can also help if your included template starts with a line dedicated to load tags libraries :

```django
{% load somelibrary %}
add-something-here
```

With the first line having no content rendered, but include a newline, we have this newline in the final template

## License

`django-include-strip-tag` is published under the MIT License (see the LICENSE file)
