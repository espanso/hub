# html-colors

<!-- badges: start -->
[![Project Status: Active – The project has reached a stable, usable
state and is being actively
developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![License:
MIT](https://img.shields.io/badge/license-MIT-green)](https://choosealicense.com/licenses/mit/)
<!-- badges: end -->

## Overview

`html-colors` is an [Espanso](https://espanso.org) package that allows
you to insert HTML color codes into your text seamlessly. By using this
package, shortcuts like `##red` are automatically replaced with their
corresponding hex color codes (e.g., `#FF0000`). You can also retrieve
RGB color codes and the color family. It is designed to work in
conjunction with the
[`html-utils-package`](https://hub.espanso.org/html-utils-package).

This package is inspired by [Jenny Knuth’s
gist](https://gist.github.com/jennyknuth/e2d9ee930303d5a5fe8862c6e31819c5).
A big thank you to Jenny!

## Installation

To install the latest released version of `html-colors`, use [Espanso
Hub](https://hub.espanso.org/):

``` sh
espanso install html-colors
```

To install the development version directly from GitHub, use:

``` sh
espanso install html-colors --git https://github.com/danielvartan/html-colors/ --external
```

## Usage

Once installed, `html-colors` will replace the specified shortcuts with
their corresponding character as you type.

| Trigger                           | Result                             | Color                          |
|-----------------------------------|------------------------------------|--------------------------------|
| `##indianred`                     | `#CD5C5C`                          | ![\#CD5C5C](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/CD5C5C.png) |
| `##rgb-indianred`                 | `205, 92, 92`                      | ![\#CD5C5C](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/CD5C5C.png) |
| `##families-indianred`            | `red, brown`                       | ![\#CD5C5C](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/CD5C5C.png) |
| `##lightcoral`                    | `#F08080`                          | ![\#F08080](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F08080.png) |
| `##rgb-lightcoral`                | `240, 128, 128`                    | ![\#F08080](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F08080.png) |
| `##families-lightcoral`           | `red, pink, coral, light`          | ![\#F08080](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F08080.png) |
| `##salmon`                        | `#FA8072`                          | ![\#FA8072](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FA8072.png) |
| `##rgb-salmon`                    | `250, 128, 114`                    | ![\#FA8072](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FA8072.png) |
| `##families-salmon`               | `red, pink, orange, salmon`        | ![\#FA8072](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FA8072.png) |
| `##darksalmon`                    | `#E9967A`                          | ![\#E9967A](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/E9967A.png) |
| `##rgb-darksalmon`                | `233, 150, 122`                    | ![\#E9967A](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/E9967A.png) |
| `##families-darksalmon`           | `red, pink, orange, salmon, dark`  | ![\#E9967A](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/E9967A.png) |
| `##lightsalmon`                   | `#FFA07A`                          | ![\#FFA07A](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFA07A.png) |
| `##rgb-lightsalmon`               | `255, 160, 122`                    | ![\#FFA07A](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFA07A.png) |
| `##families-lightsalmon`          | `red, pink, orange, salmon, light` | ![\#FFA07A](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFA07A.png) |
| `##crimson`                       | `#DC143C`                          | ![\#DC143C](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DC143C.png) |
| `##rgb-crimson`                   | `220, 20, 60`                      | ![\#DC143C](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DC143C.png) |
| `##families-crimson`              | `red`                              | ![\#DC143C](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DC143C.png) |
| `##red`                           | `#FF0000`                          | ![\#FF0000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF0000.png) |
| `##rgb-red`                       | `255, 0, 0`                        | ![\#FF0000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF0000.png) |
| `##families-red`                  | `red`                              | ![\#FF0000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF0000.png) |
| `##darkred`                       | `#8B0000`                          | ![\#8B0000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8B0000.png) |
| `##rgb-darkred`                   | `139, 0, 0`                        | ![\#8B0000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8B0000.png) |
| `##families-darkred`              | `red, dark`                        | ![\#8B0000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8B0000.png) |
| `##pink`                          | `#FFC0CB`                          | ![\#FFC0CB](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFC0CB.png) |
| `##rgb-pink`                      | `255, 192, 203`                    | ![\#FFC0CB](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFC0CB.png) |
| `##families-pink`                 | `pink`                             | ![\#FFC0CB](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFC0CB.png) |
| `##lightpink`                     | `#FFB6C1`                          | ![\#FFB6C1](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFB6C1.png) |
| `##rgb-lightpink`                 | `255, 182, 193`                    | ![\#FFB6C1](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFB6C1.png) |
| `##families-lightpink`            | `pink, light`                      | ![\#FFB6C1](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFB6C1.png) |
| `##hotpink`                       | `#FF69B4`                          | ![\#FF69B4](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF69B4.png) |
| `##rgb-hotpink`                   | `255, 105, 180`                    | ![\#FF69B4](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF69B4.png) |
| `##families-hotpink`              | `pink, hot`                        | ![\#FF69B4](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF69B4.png) |
| `##deeppink`                      | `#FF1493`                          | ![\#FF1493](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF1493.png) |
| `##rgb-deeppink`                  | `255, 20, 147`                     | ![\#FF1493](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF1493.png) |
| `##families-deeppink`             | `pink, deep`                       | ![\#FF1493](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF1493.png) |
| `##mediumvioletred`               | `#C71585`                          | ![\#C71585](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/C71585.png) |
| `##rgb-mediumvioletred`           | `199, 21, 133`                     | ![\#C71585](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/C71585.png) |
| `##families-mediumvioletred`      | `pink, purple, violet, medium`     | ![\#C71585](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/C71585.png) |
| `##palevioletred`                 | `#DB7093`                          | ![\#DB7093](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DB7093.png) |
| `##rgb-palevioletred`             | `219, 112, 147`                    | ![\#DB7093](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DB7093.png) |
| `##families-palevioletred`        | `pink, pale, violet`               | ![\#DB7093](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DB7093.png) |
| `##coral`                         | `#FF7F50`                          | ![\#FF7F50](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF7F50.png) |
| `##rgb-coral`                     | `255, 127, 80`                     | ![\#FF7F50](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF7F50.png) |
| `##families-coral`                | `orange, coral`                    | ![\#FF7F50](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF7F50.png) |
| `##tomato`                        | `#FF6347`                          | ![\#FF6347](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF6347.png) |
| `##rgb-tomato`                    | `255, 99, 71`                      | ![\#FF6347](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF6347.png) |
| `##families-tomato`               | `orange, red`                      | ![\#FF6347](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF6347.png) |
| `##orangered`                     | `#FF4500`                          | ![\#FF4500](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF4500.png) |
| `##rgb-orangered`                 | `255, 69, 0`                       | ![\#FF4500](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF4500.png) |
| `##families-orangered`            | `orange, red`                      | ![\#FF4500](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF4500.png) |
| `##darkorange`                    | `#FF8C00`                          | ![\#FF8C00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF8C00.png) |
| `##rgb-darkorange`                | `255, 140, 0`                      | ![\#FF8C00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF8C00.png) |
| `##families-darkorange`           | `orange, dark`                     | ![\#FF8C00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF8C00.png) |
| `##orange`                        | `#FFA500`                          | ![\#FFA500](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFA500.png) |
| `##rgb-orange`                    | `255, 165, 0`                      | ![\#FFA500](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFA500.png) |
| `##families-orange`               | `orange`                           | ![\#FFA500](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFA500.png) |
| `##gold`                          | `#FFD700`                          | ![\#FFD700](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFD700.png) |
| `##rgb-gold`                      | `255, 215, 0`                      | ![\#FFD700](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFD700.png) |
| `##families-gold`                 | `yellow`                           | ![\#FFD700](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFD700.png) |
| `##yellow`                        | `#FFFF00`                          | ![\#FFFF00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFF00.png) |
| `##rgb-yellow`                    | `255, 255, 0`                      | ![\#FFFF00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFF00.png) |
| `##families-yellow`               | `yellow`                           | ![\#FFFF00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFF00.png) |
| `##lightyellow`                   | `#FFFFE0`                          | ![\#FFFFE0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFFE0.png) |
| `##rgb-lightyellow`               | `255, 255, 224`                    | ![\#FFFFE0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFFE0.png) |
| `##families-lightyellow`          | `yellow, light`                    | ![\#FFFFE0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFFE0.png) |
| `##lemonchiffon`                  | `#FFFACD`                          | ![\#FFFACD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFACD.png) |
| `##rgb-lemonchiffon`              | `255, 250, 205`                    | ![\#FFFACD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFACD.png) |
| `##families-lemonchiffon`         | `yellow, lemon`                    | ![\#FFFACD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFACD.png) |
| `##lightgoldenrodyellow`          | `#FAFAD2`                          | ![\#FAFAD2](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FAFAD2.png) |
| `##rgb-lightgoldenrodyellow`      | `250, 250, 210`                    | ![\#FAFAD2](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FAFAD2.png) |
| `##families-lightgoldenrodyellow` | `yellow, light, goldenrod, tan`    | ![\#FAFAD2](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FAFAD2.png) |
| `##papayawhip`                    | `#FFEFD5`                          | ![\#FFEFD5](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFEFD5.png) |
| `##rgb-papayawhip`                | `255, 239, 213`                    | ![\#FFEFD5](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFEFD5.png) |
| `##families-papayawhip`           | `pink, tan`                        | ![\#FFEFD5](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFEFD5.png) |
| `##moccasin`                      | `#FFE4B5`                          | ![\#FFE4B5](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFE4B5.png) |
| `##rgb-moccasin`                  | `255, 228, 181`                    | ![\#FFE4B5](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFE4B5.png) |
| `##families-moccasin`             | `pink, tan`                        | ![\#FFE4B5](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFE4B5.png) |
| `##peachpuff`                     | `#FFDAB9`                          | ![\#FFDAB9](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFDAB9.png) |
| `##rgb-peachpuff`                 | `255, 218, 185`                    | ![\#FFDAB9](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFDAB9.png) |
| `##families-peachpuff`            | `pink, orange, peach`              | ![\#FFDAB9](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFDAB9.png) |
| `##palegoldenrod`                 | `#EEE8AA`                          | ![\#EEE8AA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/EEE8AA.png) |
| `##rgb-palegoldenrod`             | `238, 232, 170`                    | ![\#EEE8AA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/EEE8AA.png) |
| `##families-palegoldenrod`        | `yellow, tan, pale, goldenrod`     | ![\#EEE8AA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/EEE8AA.png) |
| `##khaki`                         | `#F0E68C`                          | ![\#F0E68C](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F0E68C.png) |
| `##rgb-khaki`                     | `240, 230, 140`                    | ![\#F0E68C](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F0E68C.png) |
| `##families-khaki`                | `yellow, tan, khaki`               | ![\#F0E68C](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F0E68C.png) |
| `##darkkhaki`                     | `#BDB76B`                          | ![\#BDB76B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/BDB76B.png) |
| `##rgb-darkkhaki`                 | `189, 183, 107`                    | ![\#BDB76B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/BDB76B.png) |
| `##families-darkkhaki`            | `yellow, tan, khaki, dark`         | ![\#BDB76B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/BDB76B.png) |
| `##lavender`                      | `#E6E6FA`                          | ![\#E6E6FA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/E6E6FA.png) |
| `##rgb-lavender`                  | `230, 230, 250`                    | ![\#E6E6FA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/E6E6FA.png) |
| `##families-lavender`             | `purple`                           | ![\#E6E6FA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/E6E6FA.png) |
| `##thistle`                       | `#D8BFD8`                          | ![\#D8BFD8](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/D8BFD8.png) |
| `##rgb-thistle`                   | `216, 191, 216`                    | ![\#D8BFD8](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/D8BFD8.png) |
| `##families-thistle`              | `purple`                           | ![\#D8BFD8](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/D8BFD8.png) |
| `##plum`                          | `#DDA0DD`                          | ![\#DDA0DD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DDA0DD.png) |
| `##rgb-plum`                      | `221, 160, 221`                    | ![\#DDA0DD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DDA0DD.png) |
| `##families-plum`                 | `purple`                           | ![\#DDA0DD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DDA0DD.png) |
| `##violet`                        | `#EE82EE`                          | ![\#EE82EE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/EE82EE.png) |
| `##rgb-violet`                    | `238, 130, 238`                    | ![\#EE82EE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/EE82EE.png) |
| `##families-violet`               | `purple, violet, pink`             | ![\#EE82EE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/EE82EE.png) |
| `##orchid`                        | `#DA70D6`                          | ![\#DA70D6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DA70D6.png) |
| `##rgb-orchid`                    | `218, 112, 214`                    | ![\#DA70D6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DA70D6.png) |
| `##families-orchid`               | `purple, orchid`                   | ![\#DA70D6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DA70D6.png) |
| `##fuchsia`                       | `#FF00FF`                          | ![\#FF00FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF00FF.png) |
| `##rgb-fuchsia`                   | `255, 0, 255`                      | ![\#FF00FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF00FF.png) |
| `##families-fuchsia`              | `purple, pink`                     | ![\#FF00FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF00FF.png) |
| `##magenta`                       | `#FF00FF`                          | ![\#FF00FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF00FF.png) |
| `##rgb-magenta`                   | `255, 0, 255`                      | ![\#FF00FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF00FF.png) |
| `##families-magenta`              | `purple, pink, magenta`            | ![\#FF00FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FF00FF.png) |
| `##mediumorchid`                  | `#BA55D3`                          | ![\#BA55D3](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/BA55D3.png) |
| `##rgb-mediumorchid`              | `186, 85, 211`                     | ![\#BA55D3](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/BA55D3.png) |
| `##families-mediumorchid`         | `purple, orchid, medium`           | ![\#BA55D3](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/BA55D3.png) |
| `##mediumpurple`                  | `#9370DB`                          | ![\#9370DB](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/9370DB.png) |
| `##rgb-mediumpurple`              | `147, 112, 219`                    | ![\#9370DB](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/9370DB.png) |
| `##families-mediumpurple`         | `purple, medium`                   | ![\#9370DB](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/9370DB.png) |
| `##rebeccapurple`                 | `#663399`                          | ![\#663399](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/663399.png) |
| `##rgb-rebeccapurple`             | `102, 51, 153`                     | ![\#663399](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/663399.png) |
| `##families-rebeccapurple`        | `purple, blue`                     | ![\#663399](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/663399.png) |
| `##blueviolet`                    | `#8A2BE2`                          | ![\#8A2BE2](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8A2BE2.png) |
| `##rgb-blueviolet`                | `138, 43, 226`                     | ![\#8A2BE2](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8A2BE2.png) |
| `##families-blueviolet`           | `purple, blue, violet`             | ![\#8A2BE2](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8A2BE2.png) |
| `##darkviolet`                    | `#9400D3`                          | ![\#9400D3](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/9400D3.png) |
| `##rgb-darkviolet`                | `148, 0, 211`                      | ![\#9400D3](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/9400D3.png) |
| `##families-darkviolet`           | `purple, dark, violet`             | ![\#9400D3](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/9400D3.png) |
| `##darkorchid`                    | `#9932CC`                          | ![\#9932CC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/9932CC.png) |
| `##rgb-darkorchid`                | `153, 50, 204`                     | ![\#9932CC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/9932CC.png) |
| `##families-darkorchid`           | `purple, dark, orchid`             | ![\#9932CC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/9932CC.png) |
| `##darkmagenta`                   | `#8B008B`                          | ![\#8B008B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8B008B.png) |
| `##rgb-darkmagenta`               | `139, 0, 139`                      | ![\#8B008B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8B008B.png) |
| `##families-darkmagenta`          | `purple, dark, magenta`            | ![\#8B008B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8B008B.png) |
| `##purple`                        | `#800080`                          | ![\#800080](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/800080.png) |
| `##rgb-purple`                    | `128, 0, 128`                      | ![\#800080](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/800080.png) |
| `##families-purple`               | `purple`                           | ![\#800080](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/800080.png) |
| `##indigo`                        | `#4B0082`                          | ![\#4B0082](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/4B0082.png) |
| `##rgb-indigo`                    | `75, 0, 130`                       | ![\#4B0082](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/4B0082.png) |
| `##families-indigo`               | `purple, blue`                     | ![\#4B0082](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/4B0082.png) |
| `##slateblue`                     | `#6A5ACD`                          | ![\#6A5ACD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/6A5ACD.png) |
| `##rgb-slateblue`                 | `106, 90, 205`                     | ![\#6A5ACD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/6A5ACD.png) |
| `##families-slateblue`            | `purple, blue, slate`              | ![\#6A5ACD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/6A5ACD.png) |
| `##darkslateblue`                 | `#483D8B`                          | ![\#483D8B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/483D8B.png) |
| `##rgb-darkslateblue`             | `72, 61, 139`                      | ![\#483D8B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/483D8B.png) |
| `##families-darkslateblue`        | `purple, blue, slate, dark`        | ![\#483D8B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/483D8B.png) |
| `##mediumslateblue`               | `#7B68EE`                          | ![\#7B68EE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/7B68EE.png) |
| `##rgb-mediumslateblue`           | `123, 104, 238`                    | ![\#7B68EE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/7B68EE.png) |
| `##families-mediumslateblue`      | `purple, blue, slate, medium`      | ![\#7B68EE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/7B68EE.png) |
| `##greenyellow`                   | `#ADFF2F`                          | ![\#ADFF2F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/ADFF2F.png) |
| `##rgb-greenyellow`               | `173, 255, 47`                     | ![\#ADFF2F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/ADFF2F.png) |
| `##families-greenyellow`          | `green, yellow`                    | ![\#ADFF2F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/ADFF2F.png) |
| `##chartreuse`                    | `#7FFF00`                          | ![\#7FFF00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/7FFF00.png) |
| `##rgb-chartreuse`                | `127, 255, 0`                      | ![\#7FFF00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/7FFF00.png) |
| `##families-chartreuse`           | `green`                            | ![\#7FFF00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/7FFF00.png) |
| `##lawngreen`                     | `#7CFC00`                          | ![\#7CFC00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/7CFC00.png) |
| `##rgb-lawngreen`                 | `124, 252, 0`                      | ![\#7CFC00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/7CFC00.png) |
| `##families-lawngreen`            | `green`                            | ![\#7CFC00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/7CFC00.png) |
| `##lime`                          | `#00FF00`                          | ![\#00FF00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FF00.png) |
| `##rgb-lime`                      | `0, 255, 0`                        | ![\#00FF00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FF00.png) |
| `##families-lime`                 | `green`                            | ![\#00FF00](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FF00.png) |
| `##limegreen`                     | `#32CD32`                          | ![\#32CD32](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/32CD32.png) |
| `##rgb-limegreen`                 | `50, 205, 50`                      | ![\#32CD32](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/32CD32.png) |
| `##families-limegreen`            | `green`                            | ![\#32CD32](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/32CD32.png) |
| `##palegreen`                     | `#98FB98`                          | ![\#98FB98](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/98FB98.png) |
| `##rgb-palegreen`                 | `152, 251, 152`                    | ![\#98FB98](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/98FB98.png) |
| `##families-palegreen`            | `green, pale`                      | ![\#98FB98](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/98FB98.png) |
| `##lightgreen`                    | `#90EE90`                          | ![\#90EE90](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/90EE90.png) |
| `##rgb-lightgreen`                | `144, 238, 144`                    | ![\#90EE90](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/90EE90.png) |
| `##families-lightgreen`           | `green, light`                     | ![\#90EE90](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/90EE90.png) |
| `##mediumspringgreen`             | `#00FA9A`                          | ![\#00FA9A](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FA9A.png) |
| `##rgb-mediumspringgreen`         | `0, 250, 154`                      | ![\#00FA9A](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FA9A.png) |
| `##families-mediumspringgreen`    | `green, medium, spring`            | ![\#00FA9A](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FA9A.png) |
| `##springgreen`                   | `#00FF7F`                          | ![\#00FF7F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FF7F.png) |
| `##rgb-springgreen`               | `0, 255, 127`                      | ![\#00FF7F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FF7F.png) |
| `##families-springgreen`          | `green, spring`                    | ![\#00FF7F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FF7F.png) |
| `##mediumseagreen`                | `#3CB371`                          | ![\#3CB371](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/3CB371.png) |
| `##rgb-mediumseagreen`            | `60, 179, 113`                     | ![\#3CB371](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/3CB371.png) |
| `##families-mediumseagreen`       | `green, sea, medium`               | ![\#3CB371](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/3CB371.png) |
| `##seagreen`                      | `#2E8B57`                          | ![\#2E8B57](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/2E8B57.png) |
| `##rgb-seagreen`                  | `46, 139, 87`                      | ![\#2E8B57](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/2E8B57.png) |
| `##families-seagreen`             | `green, sea`                       | ![\#2E8B57](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/2E8B57.png) |
| `##forestgreen`                   | `#228B22`                          | ![\#228B22](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/228B22.png) |
| `##rgb-forestgreen`               | `34, 139, 34`                      | ![\#228B22](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/228B22.png) |
| `##families-forestgreen`          | `green, forest`                    | ![\#228B22](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/228B22.png) |
| `##green`                         | `#008000`                          | ![\#008000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/008000.png) |
| `##rgb-green`                     | `0, 128, 0`                        | ![\#008000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/008000.png) |
| `##families-green`                | `green`                            | ![\#008000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/008000.png) |
| `##darkgreen`                     | `#006400`                          | ![\#006400](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/006400.png) |
| `##rgb-darkgreen`                 | `0, 100, 0`                        | ![\#006400](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/006400.png) |
| `##families-darkgreen`            | `green, dark`                      | ![\#006400](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/006400.png) |
| `##yellowgreen`                   | `#9ACD32`                          | ![\#9ACD32](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/9ACD32.png) |
| `##rgb-yellowgreen`               | `154, 205, 50`                     | ![\#9ACD32](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/9ACD32.png) |
| `##families-yellowgreen`          | `green, yellow`                    | ![\#9ACD32](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/9ACD32.png) |
| `##olivedrab`                     | `#6B8E23`                          | ![\#6B8E23](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/6B8E23.png) |
| `##rgb-olivedrab`                 | `107, 142, 35`                     | ![\#6B8E23](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/6B8E23.png) |
| `##families-olivedrab`            | `green, olive`                     | ![\#6B8E23](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/6B8E23.png) |
| `##olive`                         | `#6B8E23`                          | ![\#6B8E23](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/6B8E23.png) |
| `##rgb-olive`                     | `128, 128, 0`                      | ![\#6B8E23](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/6B8E23.png) |
| `##families-olive`                | `green, olive`                     | ![\#6B8E23](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/6B8E23.png) |
| `##darkolivegreen`                | `#556B2F`                          | ![\#556B2F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/556B2F.png) |
| `##rgb-darkolivegreen`            | `85, 107, 47`                      | ![\#556B2F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/556B2F.png) |
| `##families-darkolivegreen`       | `green, olive, dark`               | ![\#556B2F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/556B2F.png) |
| `##mediumaquamarine`              | `#66CDAA`                          | ![\#66CDAA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/66CDAA.png) |
| `##rgb-mediumaquamarine`          | `102, 205, 170`                    | ![\#66CDAA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/66CDAA.png) |
| `##families-mediumaquamarine`     | `green, blue, aquamarine, medium`  | ![\#66CDAA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/66CDAA.png) |
| `##darkseagreen`                  | `#8FBC8B`                          | ![\#8FBC8B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8FBC8B.png) |
| `##rgb-darkseagreen`              | `143, 188, 139`                    | ![\#8FBC8B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8FBC8B.png) |
| `##families-darkseagreen`         | `green, sea, dark`                 | ![\#8FBC8B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8FBC8B.png) |
| `##lightseagreen`                 | `#20B2AA`                          | ![\#20B2AA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/20B2AA.png) |
| `##rgb-lightseagreen`             | `32, 178, 170`                     | ![\#20B2AA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/20B2AA.png) |
| `##families-lightseagreen`        | `green, blue, sea, light`          | ![\#20B2AA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/20B2AA.png) |
| `##darkcyan`                      | `#008B8B`                          | ![\#008B8B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/008B8B.png) |
| `##rgb-darkcyan`                  | `0, 139, 139`                      | ![\#008B8B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/008B8B.png) |
| `##families-darkcyan`             | `green, blue, cyan, dark`          | ![\#008B8B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/008B8B.png) |
| `##teal`                          | `#008080`                          | ![\#008080](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/008080.png) |
| `##rgb-teal`                      | `0, 128, 128`                      | ![\#008080](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/008080.png) |
| `##families-teal`                 | `green, blue`                      | ![\#008080](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/008080.png) |
| `##aqua`                          | `#00FFFF`                          | ![\#00FFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FFFF.png) |
| `##rgb-aqua`                      | `0, 255, 255`                      | ![\#00FFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FFFF.png) |
| `##families-aqua`                 | `blue, aqua`                       | ![\#00FFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FFFF.png) |
| `##cyan`                          | `#00FFFF`                          | ![\#00FFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FFFF.png) |
| `##rgb-cyan`                      | `0, 255, 255`                      | ![\#00FFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FFFF.png) |
| `##families-cyan`                 | `blue, cyan`                       | ![\#00FFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00FFFF.png) |
| `##lightcyan`                     | `#E0FFFF`                          | ![\#E0FFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/E0FFFF.png) |
| `##rgb-lightcyan`                 | `224, 255, 255`                    | ![\#E0FFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/E0FFFF.png) |
| `##families-lightcyan`            | `blue, cyan, light`                | ![\#E0FFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/E0FFFF.png) |
| `##paleturquoise`                 | `#AFEEEE`                          | ![\#AFEEEE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/AFEEEE.png) |
| `##rgb-paleturquoise`             | `175, 238, 238`                    | ![\#AFEEEE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/AFEEEE.png) |
| `##families-paleturquoise`        | `blue, turquoise, pale`            | ![\#AFEEEE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/AFEEEE.png) |
| `##aquamarine`                    | `#7FFFD4`                          | ![\#7FFFD4](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/7FFFD4.png) |
| `##rgb-aquamarine`                | `127, 255, 212`                    | ![\#7FFFD4](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/7FFFD4.png) |
| `##families-aquamarine`           | `blue, aquamarine`                 | ![\#7FFFD4](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/7FFFD4.png) |
| `##turquoise`                     | `#40E0D0`                          | ![\#40E0D0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/40E0D0.png) |
| `##rgb-turquoise`                 | `64, 224, 208`                     | ![\#40E0D0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/40E0D0.png) |
| `##families-turquoise`            | `blue, turquoise`                  | ![\#40E0D0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/40E0D0.png) |
| `##mediumturquoise`               | `#48D1CC`                          | ![\#48D1CC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/48D1CC.png) |
| `##rgb-mediumturquoise`           | `72, 209, 204`                     | ![\#48D1CC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/48D1CC.png) |
| `##families-mediumturquoise`      | `blue, turquoise, medium`          | ![\#48D1CC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/48D1CC.png) |
| `##darkturquoise`                 | `#00CED1`                          | ![\#00CED1](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00CED1.png) |
| `##rgb-darkturquoise`             | `0, 206, 209`                      | ![\#00CED1](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00CED1.png) |
| `##families-darkturquoise`        | `blue, turquoise, dark`            | ![\#00CED1](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00CED1.png) |
| `##cadetblue`                     | `#5F9EA0`                          | ![\#5F9EA0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/5F9EA0.png) |
| `##rgb-cadetblue`                 | `95, 158, 160`                     | ![\#5F9EA0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/5F9EA0.png) |
| `##families-cadetblue`            | `blue, gray`                       | ![\#5F9EA0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/5F9EA0.png) |
| `##steelblue`                     | `#4682B4`                          | ![\#4682B4](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/4682B4.png) |
| `##rgb-steelblue`                 | `70, 130, 180`                     | ![\#4682B4](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/4682B4.png) |
| `##families-steelblue`            | `blue, steel`                      | ![\#4682B4](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/4682B4.png) |
| `##lightsteelblue`                | `#B0C4DE`                          | ![\#B0C4DE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/B0C4DE.png) |
| `##rgb-lightsteelblue`            | `176, 196, 222`                    | ![\#B0C4DE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/B0C4DE.png) |
| `##families-lightsteelblue`       | `blue, steel, light`               | ![\#B0C4DE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/B0C4DE.png) |
| `##powderblue`                    | `#B0E0E6`                          | ![\#B0E0E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/B0E0E6.png) |
| `##rgb-powderblue`                | `176, 224, 230`                    | ![\#B0E0E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/B0E0E6.png) |
| `##families-powderblue`           | `blue`                             | ![\#B0E0E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/B0E0E6.png) |
| `##lightblue`                     | `#ADD8E6`                          | ![\#ADD8E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/ADD8E6.png) |
| `##rgb-lightblue`                 | `173, 216, 230`                    | ![\#ADD8E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/ADD8E6.png) |
| `##families-lightblue`            | `blue, light`                      | ![\#ADD8E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/ADD8E6.png) |
| `##skyblue`                       | `#87CEEB`                          | ![\#87CEEB](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/87CEEB.png) |
| `##rgb-skyblue`                   | `135, 206, 235`                    | ![\#87CEEB](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/87CEEB.png) |
| `##families-skyblue`              | `blue, sky`                        | ![\#87CEEB](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/87CEEB.png) |
| `##lightskyblue`                  | `#87CEFA`                          | ![\#87CEFA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/87CEFA.png) |
| `##rgb-lightskyblue`              | `135, 206, 250`                    | ![\#87CEFA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/87CEFA.png) |
| `##families-lightskyblue`         | `blue, sky, light`                 | ![\#87CEFA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/87CEFA.png) |
| `##deepskyblue`                   | `#00BFFF`                          | ![\#00BFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00BFFF.png) |
| `##rgb-deepskyblue`               | `0, 191, 255`                      | ![\#00BFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00BFFF.png) |
| `##families-deepskyblue`          | `blue, sky, deep`                  | ![\#00BFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00BFFF.png) |
| `##dodgerblue`                    | `#1E90FF`                          | ![\#1E90FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/1E90FF.png) |
| `##rgb-dodgerblue`                | `30, 144, 255`                     | ![\#1E90FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/1E90FF.png) |
| `##families-dodgerblue`           | `blue`                             | ![\#1E90FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/1E90FF.png) |
| `##cornflowerblue`                | `#6495ED`                          | ![\#6495ED](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/6495ED.png) |
| `##rgb-cornflowerblue`            | `100, 149, 237`                    | ![\#6495ED](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/6495ED.png) |
| `##families-cornflowerblue`       | `blue`                             | ![\#6495ED](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/6495ED.png) |
| `##royalblue`                     | `#4169E1`                          | ![\#4169E1](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/4169E1.png) |
| `##rgb-royalblue`                 | `65, 105, 225`                     | ![\#4169E1](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/4169E1.png) |
| `##families-royalblue`            | `blue`                             | ![\#4169E1](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/4169E1.png) |
| `##blue`                          | `#0000FF`                          | ![\#0000FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/0000FF.png) |
| `##rgb-blue`                      | `0, 0, 255`                        | ![\#0000FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/0000FF.png) |
| `##families-blue`                 | `blue`                             | ![\#0000FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/0000FF.png) |
| `##mediumblue`                    | `#0000CD`                          | ![\#0000CD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/0000CD.png) |
| `##rgb-mediumblue`                | `0, 0, 205`                        | ![\#0000CD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/0000CD.png) |
| `##families-mediumblue`           | `blue, medium`                     | ![\#0000CD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/0000CD.png) |
| `##darkblue`                      | `#00008B`                          | ![\#00008B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00008B.png) |
| `##rgb-darkblue`                  | `0, 0, 139`                        | ![\#00008B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00008B.png) |
| `##families-darkblue`             | `blue, dark`                       | ![\#00008B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00008B.png) |
| `##navy`                          | `#00008B`                          | ![\#00008B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00008B.png) |
| `##rgb-navy`                      | `0, 0, 128`                        | ![\#00008B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00008B.png) |
| `##families-navy`                 | `blue, dark`                       | ![\#00008B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/00008B.png) |
| `##midnightblue`                  | `#191970`                          | ![\#191970](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/191970.png) |
| `##rgb-midnightblue`              | `25, 25, 112`                      | ![\#191970](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/191970.png) |
| `##families-midnightblue`         | `blue, dark`                       | ![\#191970](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/191970.png) |
| `##cornsilk`                      | `#FFF8DC`                          | ![\#FFF8DC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFF8DC.png) |
| `##rgb-cornsilk`                  | `255, 248, 220`                    | ![\#FFF8DC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFF8DC.png) |
| `##families-cornsilk`             | `brown, tan`                       | ![\#FFF8DC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFF8DC.png) |
| `##blanchedalmond`                | `#FFEBCD`                          | ![\#FFEBCD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFEBCD.png) |
| `##rgb-blanchedalmond`            | `255, 235, 205`                    | ![\#FFEBCD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFEBCD.png) |
| `##families-blanchedalmond`       | `brown, tan`                       | ![\#FFEBCD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFEBCD.png) |
| `##bisque`                        | `#FFE4C4`                          | ![\#FFE4C4](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFE4C4.png) |
| `##rgb-bisque`                    | `255, 228, 196`                    | ![\#FFE4C4](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFE4C4.png) |
| `##families-bisque`               | `brown, tan`                       | ![\#FFE4C4](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFE4C4.png) |
| `##navajowhite`                   | `#FFDEAD`                          | ![\#FFDEAD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFDEAD.png) |
| `##rgb-navajowhite`               | `255, 222, 173`                    | ![\#FFDEAD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFDEAD.png) |
| `##families-navajowhite`          | `brown, tan`                       | ![\#FFDEAD](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFDEAD.png) |
| `##wheat`                         | `#F5DEB3`                          | ![\#F5DEB3](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F5DEB3.png) |
| `##rgb-wheat`                     | `245, 222, 179`                    | ![\#F5DEB3](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F5DEB3.png) |
| `##families-wheat`                | `brown, tan`                       | ![\#F5DEB3](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F5DEB3.png) |
| `##burlywood`                     | `#DEB887`                          | ![\#DEB887](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DEB887.png) |
| `##rgb-burlywood`                 | `222, 184, 135`                    | ![\#DEB887](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DEB887.png) |
| `##families-burlywood`            | `brown, tan`                       | ![\#DEB887](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DEB887.png) |
| `##tan`                           | `#D2B48C`                          | ![\#D2B48C](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/D2B48C.png) |
| `##rgb-tan`                       | `210, 180, 140`                    | ![\#D2B48C](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/D2B48C.png) |
| `##families-tan`                  | `brown, tan`                       | ![\#D2B48C](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/D2B48C.png) |
| `##rosybrown`                     | `#BC8F8F`                          | ![\#BC8F8F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/BC8F8F.png) |
| `##rgb-rosybrown`                 | `188, 143, 143`                    | ![\#BC8F8F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/BC8F8F.png) |
| `##families-rosybrown`            | `brown, tan`                       | ![\#BC8F8F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/BC8F8F.png) |
| `##sandybrown`                    | `#F4A460`                          | ![\#F4A460](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F4A460.png) |
| `##rgb-sandybrown`                | `244, 164, 96`                     | ![\#F4A460](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F4A460.png) |
| `##families-sandybrown`           | `brown, orange`                    | ![\#F4A460](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F4A460.png) |
| `##goldenrod`                     | `#DAA520`                          | ![\#DAA520](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DAA520.png) |
| `##rgb-goldenrod`                 | `218, 165, 32`                     | ![\#DAA520](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DAA520.png) |
| `##families-goldenrod`            | `brown, goldenrod, orange`         | ![\#DAA520](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DAA520.png) |
| `##darkgoldenrod`                 | `#B8860B`                          | ![\#B8860B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/B8860B.png) |
| `##rgb-darkgoldenrod`             | `184, 134, 11`                     | ![\#B8860B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/B8860B.png) |
| `##families-darkgoldenrod`        | `brown, orange, goldenrod, dark`   | ![\#B8860B](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/B8860B.png) |
| `##peru`                          | `#CD853F`                          | ![\#CD853F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/CD853F.png) |
| `##rgb-peru`                      | `205, 133, 63`                     | ![\#CD853F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/CD853F.png) |
| `##families-peru`                 | `brown, orange`                    | ![\#CD853F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/CD853F.png) |
| `##chocolate`                     | `#D2691E`                          | ![\#D2691E](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/D2691E.png) |
| `##rgb-chocolate`                 | `210, 105, 30`                     | ![\#D2691E](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/D2691E.png) |
| `##families-chocolate`            | `brown, orange`                    | ![\#D2691E](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/D2691E.png) |
| `##saddlebrown`                   | `#8B4513`                          | ![\#8B4513](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8B4513.png) |
| `##rgb-saddlebrown`               | `139, 69, 19`                      | ![\#8B4513](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8B4513.png) |
| `##families-saddlebrown`          | `brown`                            | ![\#8B4513](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/8B4513.png) |
| `##sienna`                        | `#A0522D`                          | ![\#A0522D](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/A0522D.png) |
| `##rgb-sienna`                    | `160, 82, 45`                      | ![\#A0522D](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/A0522D.png) |
| `##families-sienna`               | `brown`                            | ![\#A0522D](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/A0522D.png) |
| `##brown`                         | `#A52A2A`                          | ![\#A52A2A](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/A52A2A.png) |
| `##rgb-brown`                     | `165, 42, 42`                      | ![\#A52A2A](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/A52A2A.png) |
| `##families-brown`                | `brown, red`                       | ![\#A52A2A](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/A52A2A.png) |
| `##maroon`                        | `#800000`                          | ![\#800000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/800000.png) |
| `##rgb-maroon`                    | `128, 0, 0`                        | ![\#800000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/800000.png) |
| `##families-maroon`               | `brown, red`                       | ![\#800000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/800000.png) |
| `##white`                         | `#FFFFFF`                          | ![\#FFFFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFFFF.png) |
| `##rgb-white`                     | `255, 255, 255`                    | ![\#FFFFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFFFF.png) |
| `##families-white`                | `white`                            | ![\#FFFFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFFFF.png) |
| `##snow`                          | `#FFFAFA`                          | ![\#FFFAFA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFAFA.png) |
| `##rgb-snow`                      | `255, 250, 250`                    | ![\#FFFAFA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFAFA.png) |
| `##families-snow`                 | `white`                            | ![\#FFFAFA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFAFA.png) |
| `##honeydew`                      | `#F0FFF0`                          | ![\#F0FFF0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F0FFF0.png) |
| `##rgb-honeydew`                  | `240, 255, 240`                    | ![\#F0FFF0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F0FFF0.png) |
| `##families-honeydew`             | `white`                            | ![\#F0FFF0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F0FFF0.png) |
| `##mintcream`                     | `#F5FFFA`                          | ![\#F5FFFA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F5FFFA.png) |
| `##rgb-mintcream`                 | `245, 255, 250`                    | ![\#F5FFFA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F5FFFA.png) |
| `##families-mintcream`            | `white`                            | ![\#F5FFFA](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F5FFFA.png) |
| `##azure`                         | `#F0FFFF`                          | ![\#F0FFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F0FFFF.png) |
| `##rgb-azure`                     | `240, 255, 255`                    | ![\#F0FFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F0FFFF.png) |
| `##families-azure`                | `white`                            | ![\#F0FFFF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F0FFFF.png) |
| `##aliceblue`                     | `#F0F8FF`                          | ![\#F0F8FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F0F8FF.png) |
| `##rgb-aliceblue`                 | `240, 248, 255`                    | ![\#F0F8FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F0F8FF.png) |
| `##families-aliceblue`            | `white`                            | ![\#F0F8FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F0F8FF.png) |
| `##ghostwhite`                    | `#F8F8FF`                          | ![\#F8F8FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F8F8FF.png) |
| `##rgb-ghostwhite`                | `248, 248, 255`                    | ![\#F8F8FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F8F8FF.png) |
| `##families-ghostwhite`           | `white`                            | ![\#F8F8FF](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F8F8FF.png) |
| `##whitesmoke`                    | `#F5F5F5`                          | ![\#F5F5F5](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F5F5F5.png) |
| `##rgb-whitesmoke`                | `245, 245, 245`                    | ![\#F5F5F5](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F5F5F5.png) |
| `##families-whitesmoke`           | `white`                            | ![\#F5F5F5](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F5F5F5.png) |
| `##seashell`                      | `#FFF5EE`                          | ![\#FFF5EE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFF5EE.png) |
| `##rgb-seashell`                  | `255, 245, 238`                    | ![\#FFF5EE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFF5EE.png) |
| `##families-seashell`             | `white, pink`                      | ![\#FFF5EE](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFF5EE.png) |
| `##beige`                         | `#F5F5DC`                          | ![\#F5F5DC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F5F5DC.png) |
| `##rgb-beige`                     | `245, 245, 220`                    | ![\#F5F5DC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F5F5DC.png) |
| `##families-beige`                | `white, tan`                       | ![\#F5F5DC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/F5F5DC.png) |
| `##oldlace`                       | `#FDF5E6`                          | ![\#FDF5E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FDF5E6.png) |
| `##rgb-oldlace`                   | `253, 245, 230`                    | ![\#FDF5E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FDF5E6.png) |
| `##families-oldlace`              | `white, tan`                       | ![\#FDF5E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FDF5E6.png) |
| `##floralwhite`                   | `#FDF5E6`                          | ![\#FDF5E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FDF5E6.png) |
| `##rgb-floralwhite`               | `253, 245, 230`                    | ![\#FDF5E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FDF5E6.png) |
| `##families-floralwhite`          | `white, tan`                       | ![\#FDF5E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FDF5E6.png) |
| `##ivory`                         | `#FFFFF0`                          | ![\#FFFFF0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFFF0.png) |
| `##rgb-ivory`                     | `255, 255, 240`                    | ![\#FFFFF0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFFF0.png) |
| `##families-ivory`                | `white, tan`                       | ![\#FFFFF0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFFFF0.png) |
| `##antiquewhite`                  | `#FAEBD7`                          | ![\#FAEBD7](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FAEBD7.png) |
| `##rgb-antiquewhite`              | `250, 235, 215`                    | ![\#FAEBD7](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FAEBD7.png) |
| `##families-antiquewhite`         | `white, tan`                       | ![\#FAEBD7](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FAEBD7.png) |
| `##linen`                         | `#FAF0E6`                          | ![\#FAF0E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FAF0E6.png) |
| `##rgb-linen`                     | `250, 240, 230`                    | ![\#FAF0E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FAF0E6.png) |
| `##families-linen`                | `white, tan`                       | ![\#FAF0E6](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FAF0E6.png) |
| `##lavenderblush`                 | `#FFF0F5`                          | ![\#FFF0F5](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFF0F5.png) |
| `##rgb-lavenderblush`             | `255, 240, 245`                    | ![\#FFF0F5](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFF0F5.png) |
| `##families-lavenderblush`        | `white, lavender, pink`            | ![\#FFF0F5](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFF0F5.png) |
| `##mistyrose`                     | `#FFE4E1`                          | ![\#FFE4E1](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFE4E1.png) |
| `##rgb-mistyrose`                 | `255, 228, 225`                    | ![\#FFE4E1](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFE4E1.png) |
| `##families-mistyrose`            | `white, pink`                      | ![\#FFE4E1](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/FFE4E1.png) |
| `##gainsboro`                     | `#DCDCDC`                          | ![\#DCDCDC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DCDCDC.png) |
| `##rgb-gainsboro`                 | `220, 220, 220`                    | ![\#DCDCDC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DCDCDC.png) |
| `##families-gainsboro`            | `gray`                             | ![\#DCDCDC](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/DCDCDC.png) |
| `##lightgray`                     | `#D3D3D3`                          | ![\#D3D3D3](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/D3D3D3.png) |
| `##rgb-lightgray`                 | `211, 211, 211`                    | ![\#D3D3D3](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/D3D3D3.png) |
| `##families-lightgray`            | `gray, light`                      | ![\#D3D3D3](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/D3D3D3.png) |
| `##silver`                        | `#C0C0C0`                          | ![\#C0C0C0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/C0C0C0.png) |
| `##rgb-silver`                    | `192, 192, 192`                    | ![\#C0C0C0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/C0C0C0.png) |
| `##families-silver`               | `gray`                             | ![\#C0C0C0](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/C0C0C0.png) |
| `##darkgray`                      | `#A9A9A9`                          | ![\#A9A9A9](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/A9A9A9.png) |
| `##rgb-darkgray`                  | `169, 169, 169`                    | ![\#A9A9A9](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/A9A9A9.png) |
| `##families-darkgray`             | `gray, dark`                       | ![\#A9A9A9](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/A9A9A9.png) |
| `##gray`                          | `#808080`                          | ![\#808080](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/808080.png) |
| `##rgb-gray`                      | `128, 128, 128`                    | ![\#808080](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/808080.png) |
| `##families-gray`                 | `gray`                             | ![\#808080](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/808080.png) |
| `##dimgray`                       | `#696969`                          | ![\#696969](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/696969.png) |
| `##rgb-dimgray`                   | `105, 105, 105`                    | ![\#696969](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/696969.png) |
| `##families-dimgray`              | `gray`                             | ![\#696969](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/696969.png) |
| `##lightslategray`                | `#778899`                          | ![\#778899](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/778899.png) |
| `##rgb-lightslategray`            | `119, 136, 153`                    | ![\#778899](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/778899.png) |
| `##families-lightslategray`       | `gray, light, slate`               | ![\#778899](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/778899.png) |
| `##slategray`                     | `#708090`                          | ![\#708090](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/708090.png) |
| `##rgb-slategray`                 | `112, 128, 144`                    | ![\#708090](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/708090.png) |
| `##families-slategray`            | `gray, slate`                      | ![\#708090](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/708090.png) |
| `##darkslategray`                 | `#2F4F4F`                          | ![\#2F4F4F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/2F4F4F.png) |
| `##rgb-darkslategray`             | `47, 79, 79`                       | ![\#2F4F4F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/2F4F4F.png) |
| `##families-darkslategray`        | `gray, slate, dark`                | ![\#2F4F4F](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/2F4F4F.png) |
| `##black`                         | `#000000`                          | ![\#000000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/000000.png) |
| `##rgb-black`                     | `0, 0, 0`                          | ![\#000000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/000000.png) |
| `##families-black`                | `black`                            | ![\#000000](https://github.com/danielvartan/html-colors/blob/debc28344cbbcee3177104b39220287af66c6f10/images/000000.png) |

## Prefix

The `##` prefix was used to avoid conflicts with social media hashtags
and the
[`html-utils-package`](https://hub.espanso.org/html-utils-package).

## Contributing

If you feel like there’s any important tag/snippet missing, feel free to
create a Pull Request or open an
[Issue](https://github.com/danielvartan/html-colors/issues/new).

## License

[![License:
MIT](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/license/mit/)

`html-colors` code is released under the [MIT
license](https://opensource.org/license/mit/).
