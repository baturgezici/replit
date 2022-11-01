import json

def isValid(stale, latest, otjson):
  cursor = 0
  otjson = json.loads(otjson)
  for operations in otjson:
    if operations["op"] == "insert":
      stale, cursor = insert(stale, operations["chars"], cursor)
    elif operations["op"] == "delete":
      if(cursor+int(operations["count"]) > len(stale)):
        return False
      stale = delete(stale, int(operations["count"]), cursor)
    elif operations["op"] == "skip":
      if(cursor+int(operations["count"]) > len(stale)):
        return False
      cursor = skip(cursor, int(operations["count"]))
  return stale == latest

def insert(text, string, cursor):
  text = text[:cursor] + string + text[cursor:]
  cursor = cursor + len(string)
  return text, cursor
  
def delete(text, count, cursor):
  text = text[:cursor] + text[cursor+count:]
  return text
  
def skip(cursor, count):
  cursor += count
  return cursor