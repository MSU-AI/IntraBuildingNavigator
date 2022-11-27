import 'package:flutter/material.dart';
import 'package:intra_building/api.dart';

class NavigatorPage extends StatefulWidget {
  const NavigatorPage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<NavigatorPage> createState() => _NavigatorPageState();
}

class _NavigatorPageState extends State<NavigatorPage> {
  // Initial Selected Value
  String startvalue = 'Room 1100';
  String endvalue = 'Room 1100';

  // List of items in our dropdown menu
  var starts = [
    "Room 1100",
    "Room 1103",
    "Room 1105",
    "Room 1107",
    "Room 1108",
    "Room 1109",
    "Room 1118",
    "Room 1120",
    "Room 1130",
    "Room 1148",
    "Room 1202",
    "Room 1211",
    "Room 1220",
    "Room 1226",
    "Room 1228",
  ];

  var ends = [
    "Room 1100",
    "Room 1103",
    "Room 1105",
    "Room 1107",
    "Room 1108",
    "Room 1109",
    "Room 1118",
    "Room 1120",
    "Room 1130",
    "Room 1148",
    "Room 1202",
    "Room 1211",
    "Room 1220",
    "Room 1226",
    "Room 1228",
  ];

  String _path = "";

  String url = '';
  var Data;
  String QueryText = '';

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
              '\n\nFind the optimal path between 2 rooms in the Engineering Building',
              style: Theme.of(context).textTheme.bodyMedium,
            ),
            const Text(
              '\n',
            ),
            const Text(
              'Select a start location: ',
            ),
            DropdownButton(
              // Initial Value
              value: startvalue,

              // Down Arrow Icon
              icon: const Icon(Icons.keyboard_arrow_down),

              // Array list of items
              items: starts.map((String items) {
                return DropdownMenuItem(
                  value: items,
                  child: Text(items),
                );
              }).toList(),
              // After selecting the desired option,it will
              // change button value to selected value
              onChanged: (String? newValue) {
                setState(() {
                  startvalue = newValue!;
                });
              },
            ),
            const Text(
              '\n',
            ),
            const Text(
              'Choose an end location:',
            ),
            DropdownButton(
              // Initial Value
              value: endvalue,

              // Down Arrow Icon
              icon: const Icon(Icons.keyboard_arrow_down),

              // Array list of items
              items: ends.map((String items) {
                return DropdownMenuItem(
                  value: items,
                  child: Text(items),
                );
              }).toList(),
              // After selecting the desired option,it will
              // change button value to selected value
              onChanged: (String? newValue) {
                setState(() {
                  endvalue = newValue!;
                });
              },
            ),
            const Text(
              '\n',
            ),
            OutlinedButton(
              onPressed: () async {
                url = 'http://127.0.0.1:8000/getpath';
                Data = await PostData(url, {
                  "start": startvalue.toString(),
                  "end": endvalue.toString()
                });
                setState(() {
                  QueryText = Data;
                });
              },
              child: Text('Find Path'),
            ),
            const Text(
              '\n',
            ),
            Text(
              '$QueryText',
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
