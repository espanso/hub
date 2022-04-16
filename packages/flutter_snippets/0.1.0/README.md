# A package for some commonly used flutter code snippets

Code snippets taken from [awesome-flutter-snippets](https://github.com/Nash0x7E2/awesome-flutter-snippets).

## Installation

Install the package with:

``` shell
espanso install flutter-snippets
```

## Usage

This package replaces the following keywords with the associated code snippet while you're typing:

Keyword | Description
--- | ---
[`:stlw`](#stateless-widget) | Stateless widget
[`:stfl`](#statefull-widget) | Statefull widget
[`:build`](#build-method) | Build method
[`:customPainter`](#custompainter-widget) | Custom Painter widget
[`:customClipper`](#customclipper-widget) | Custom Clipper widget
[`:initS`](#initstate-method) | initState method
[`:disp`](#dispose-method) | dispose method
[`:reassemble`](#reassemble-method) | reassemble method
[`:didChangeD`](#didchangedependencies-method) | didChangeDependencies method
[`:didUpdateW`](#didupdatewidget-method) | didUpdateWidget method
[`:importM`](#import-materialdart) | Import material.dart
[`:importC`](#import-cupertinodart) | Import cupertino.dart

</br>

> ## Stateless widget
>
> ### Keyword => **:stlw**
>
> ```dart
> import 'package:flutter/material.dart';
>
> class Example extends StatelessWidget {
>  @override
>  Widget build(BuildContext context) {
>   return Container(
>    child: Text('Hello World'),
>   );
>  }
> }
> ```
<!-- -->
> ## Statefull widget
>
> ### Keyword => **:stfl**
>
> ```dart
> import 'package:flutter/material.dart';
>
> class Example extends StatefulWidget {
> @override
> _ExampleState createState() =>_ExampleState();
> }
>
> class _ExampleState extends State<Example> {
> @override
> Widget build(BuildContext context) {
>   return Container(
>    child: Text('Hello World'),
>   );
>  }
> }
> ```
<!-- -->
> ## Build method
>
> ### Keyword => **:build**
>
> ```dart
> @override
> Widget build(BuildContext context) {
>  return Container(
>   child: Text('Hello World'),
>  );
> }
> ```
<!-- -->
> ## CustomPainter widget
>
> ### Keyword => **:customPainter**
>
> ```dart
> class ExamplePainter extends CustomPainter {
> 
>  @override
>  void paint(Canvas canvas, Size size) { }
>  @override
>  bool shouldRepaint(${0:name}Painter oldDelegate) => false;
> 
>  @override
>  bool shouldRebuildSemantics(${0:name}Painter oldDelegate) => false;
> }
> ```
<!-- -->
> ## CustomClipper widget
>
> ### Keyword => **:customClipper**
>
> ```dart
> class ExampleClipper extends CustomClipper<Path> {
> 
>  @override
>  Path getClip(Size size) { }
> 
>  @override
>  bool shouldReclip(CustomClipper<Path> oldClipper) => false;
> }
> ```
<!-- -->
> ## initState method
>
> ### Keyword => **:initS**
>
> ```dart
> @override
> void  initState() {
>  // TODO: Enter your code here
>  super.initState();
> }
> ```
<!-- -->
> ## dispose method
>
> ### Keyword => **:disp**
>
> ```dart
> @override
> void  dispose() {
>  // TODO: Enter your code here
>  super.dispose();
> }
> ```
<!-- -->
> ## reassemble method
>
> ### Keyword => **:reassemble**
>
> ```dart
> @override
> void  reassemble() {
>  // TODO: Enter your code here
>  super.reassemble();
> }
> ```
<!-- -->
> ## didChangeDependencies method
>
> ### Keyword => **:didChangeD**
>
> ```dart
> @override
> void  didChangeDependencies() {
>  // TODO: Enter your code here
>  super.didChangeDependencies();
> }
> ```
<!-- -->
> ## didUpdateWidget method
>
> ### Keyword => **:didUpdateW**
>
> ```dart
> @override
> void  didUpdateWidget(Widget widget) {
>  // TODO: Enter your code here
>  super.didUpdateWidget(oldWidget);
> }
> ```
<!-- -->
> ## import material.dart
>
> ### Keyword => **:importM**
>
> ```dart
> import 'package:flutter/material.dart';
> ```
<!-- -->
> ## import cupertino.dart
>
> ### Keyword => **:importC**
>
> ```dart
> import 'package:flutter/cupertino.dart';
> ```
