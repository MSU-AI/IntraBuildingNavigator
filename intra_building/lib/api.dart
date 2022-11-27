import 'package:http/http.dart' as http;
import 'dart:io';
import 'dart:typed_data';
import 'dart:convert';

Future Getdata(url) async {
  http.Response Response = await http.get(url);
  return Response.body;
}

Future PostData(url, json_body) async {
  http.Response Response = await http.post(Uri.parse(url), body: json_body);
  return Response.body;
}

Future<Map<String, dynamic>> PostPhoto(_byteImage) async {
  Uint8List bytes;
  // bytes = Uint8List.fromList(_byteImage);
  bytes = _byteImage;
  String base64Image = base64Encode(_byteImage);
  print('reading of bytes is completed');

  var request = http.MultipartRequest(
      'POST', Uri.parse('http://127.0.0.1:8000/photo_locator'));
  request.files.add(http.MultipartFile.fromString('picture', base64Image,
      filename: "test.JPG"));
  var res = await request.send();
  final String respStr = await res.stream.bytesToString();
  Map<String, dynamic> parsed = jsonDecode(respStr);
  print(respStr);
  return parsed;
}
