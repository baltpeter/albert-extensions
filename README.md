# My Albert extensions

> A collection of various Python extensions I wrote for the Albert launcher.

This repository contains various [Python extensions](https://albertlauncher.github.io/docs/extensions/python/) I wrote for the great [Albert keyboard launcher](https://albertlauncher.github.io/).

To install the extensions, run the following command:

```
git clone https://github.com/baltpeter/albert-extensions "~/.local/share/albert/org.albert.extension.python/modules"
```

## Included extensions

### Password generator

![Generating a 30 character password](https://cdn.baltpeter.io/img/albert-pwgen-screenshot.png)

A very simple password generator. To run it, just enter `pw` followed by the length of the password you want to generate (e.g. `pw 64`).  
If no length is given, a 25 character password will be generated.

The generated passwords are deliberately only alphanumeric and don't contain any special characters.