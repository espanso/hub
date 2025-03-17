# Espanso Form Extension Shortcut

> This package allows you to quickly create a new Espanso shortcut containing a list Form extension. Please see the example below. 

## Usage

Let's say you want to create a new Espanso shortcut that will allow you to choose between different options such as a list of colors that you frequently use in styling. Or you have a list of co-worker logins that you need to use but can't always remember off-hand. You can use the Form extension to quickly generate a shortcut template to give you a list of options to choose from.

Type `:vblf` (verbose list form) in your YAML code-editor and complete the information in the popup form. Once you click `Submit` a form trigger will be pasted in its place. Further edits, such as additional options, or changing the field `type:` to `choice`, can then be inserted.

Please see [![espanso-verbose-form-template](https://img.youtube.com/vi/videoid/0.jpg)](https://www.youtube.com/watch?v=VEGv4aHV1d8)
for a short video demo of an earlier version.

```yaml
# Example usage

  - triggers: ['csscolors--', 'csscol--']
    replace: "color:  {{CSS.color_name}}"
    vars:
      - name: "CSS"
        type: form
        params:
          layout: "color_name: [[color_name]]" 
          fields:
            color_name:
              type: list
              values:
              - red
              - orange
              - black
              - white
              - green
              - blue
              - purple
              - pink
              - yellow
              - brown
              - gray
              - cyan
              - magenta
              - lime
              - teal
              - indigo
              - violet
              - fuchsia
              - aqua
              - maroon
              - navy
              - olive
              - silver
              - limegreen
              - skyblue
              - tan
```

## Source 

Please refer to the awesome documentation for verbose syntax forms here https://espanso.org/docs/matches/forms/#controls-with-the-verbose-syntax
