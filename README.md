# Telegram-Sticker-Correction
Small utility to transform low-quality semi-square images to Telegram Stickers

As a person, who is interested in customization of any kind I tried to create a Telegram sticker pack with my favourite youtuber Technoblade.

I stumbled against a problem with actually uploading all the funny images I found, because official Telegram sticker bot requires you to submit all of your stickers as 512x512 PNG images.
Such as this one, which is surely not 512x512


![Funny Technoblade meme](https://i.pinimg.com/564x/9f/37/b4/9f37b45edc29aaf8ee38857d9d3ddf15.jpg)


I felt like this might be a problem for a lot of people and decided to write a simple python script to upscale and then transform images that look rather like a square to actual 512x512 PNG images.


# Usage

First of all, all install of the dependencies
```
pip install -r requirements.txt
```

Then simply run the code

```
python3 correction.py $path_to_image_directory
```

Output will be in the `/result` directory.

# An example

The code made this square-ish image

![Funny Technoblade meme](https://i.pinimg.com/564x/9f/37/b4/9f37b45edc29aaf8ee38857d9d3ddf15.jpg)

Look like this 

![Funny Technoblade meme, but now can be used as a sticker](https://i.pinimg.com/564x/83/65/4d/83654d826adcffba59a75a4e16b57a53.jpg)