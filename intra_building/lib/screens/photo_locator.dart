import 'dart:typed_data';

import 'package:exif/exif.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';

import 'package:intra_building/api.dart';

class PhotoPage extends StatefulWidget {
  const PhotoPage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<PhotoPage> createState() => _PhotoPageState();
}

class _PhotoPageState extends State<PhotoPage> {
  String _address = "";
  String _latitude = "";
  String _longitude = "";

  String _filename = "before.png";

  XFile? _image;
  final _picker = ImagePicker();
  Uint8List? _byteImage;

  String _exifData = "";

  Future getImage() async {
    // Pick an image
    final image = await ImagePicker().pickImage(source: ImageSource.gallery);

    if (image == null) return;

    //TO convert Xfile into file
    File path = File(image.path);

    Uint8List? img = await image.readAsBytes();
    _byteImage = img;

    setState(() {
      _image = image;
      _byteImage = img;
    });

    String exif = await getExifFromFile();

    setState(() {
      _exifData = exif;
    });

    print('Image picked');
  }

  Future<String> getExifFromFile() async {
    if (_image == null) {
      return "";
    }

    var bytes = await _image!.readAsBytes();
    var tags = await readExifFromBytes(bytes);
    var sb = StringBuffer();

    tags.forEach((k, v) {
      sb.write("$k: $v \n");
    });

    return sb.toString();
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Invoke "debug painting" (press "p" in the console, choose the
          // "Toggle Debug Paint" action from the Flutter Inspector in Android
          // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
          // to see the wireframe for each widget.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          mainAxisAlignment: MainAxisAlignment.start,
          children: <Widget>[
            Text(
              '\n\nUpload your photos to see their metadata',
              style: Theme.of(context).textTheme.bodyMedium,
            ),
            const Text(
              '\n',
            ),
            if (_byteImage != null)
              Image(
                image: MemoryImage(_byteImage!),
                height: 300,
              ),
            const Text(
              '\n',
            ),
            OutlinedButton(
              onPressed: () {
                getImage();
              },
              child: Text('Choose File'),
            ),
            const Text(
              '\n',
            ),
            OutlinedButton(
              onPressed: () async {
                Map<String, dynamic> response = await PostPhoto(_byteImage);
                setState(() {
                  _address = response["address"]!;
                  _latitude = response["latitude"]!;
                  _longitude = response["longitude"]!;
                });
                // printExifOf('assets/AI_CLUB_TEST.JPG');
              },
              child: Text('Find Image Location'),
            ),
            const Text(
              '\n',
            ),
            Text(
              'Address: $_address',
            ),
            Text(
              'Latitude: $_latitude',
            ),
            Text(
              'Longitude: $_longitude',
            ),
          ],
        ),
      ),
      // floatingActionButton: FloatingActionButton(
      //   onPressed: _incrementCounter,
      //   tooltip: 'Increment',
      //   child: const Icon(Icons.add),
      // ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
