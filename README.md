# ebay-view-bot
A bot to boost viewer count for eBay listings. Simply setup a `links.py` file with the links (no cached links) and desired view count.

Forked from [washedgram/ebay-view-bot](https://github.com/washedgram/ebay-view-bot) and heavily improved upon.

## TODO
- [ ] proxy support

## Installation

```git clone https://github.com/james168ma/ebay-view-bot.git```

## What do i need to run this?
Python, Requests

- [Install Python 3.x.x](https://www.python.org/downloads/). If you have it installed correctly, typing 'python3' in your Terminal will open an interactive console where you can execute Python code.
- Install Requests: `pip install requests` - need to install python first

## Setup

- Make a file called `links.py` inside the ebay-view-bot directory and edit the file with a text editor:

```
# links.py
links_to_views = {
    "<link 1>": <number of views for link 1>,
    "<link 2>": <number of views for link 2>,
    # ...
    # ... (continue with this format for all listings)
    # ...
    "<last link>": <number of views for last link> # (no comma for last listing)
}
```

- An example `links.py` file:

```
# links.py
links_to_views = {
    "https://www.ebay.com/itm/Supreme-Raffia-Tote-Bag-Red-SS20-IN-HAND-DEADSTOCK/303616402396?hash=item46b0f2a3dc:g:pwMAAOSwPU1fA-5q": 5,
    "https://www.ebay.com/itm/Supreme-Raffia-tote-Red-Brand-new/383621615751?hash=item5951a15087:g:JYAAAOSwW1Fe-1bd": 5,
}
```

## Execution

In Terminal:

```
cd <directory you ran the git clone command>
cd ebay-view-bot
python3 main.py
```
---

### My Modifications
- added multithreading support
- added multi-link support
- updated the README.md to reflect those changes

### washedgram's Initial License

```
Copyright (c) 2020 washedgram

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```
