struct Example {
  1:i32     number=10,
  2:i64     big_number,
  3:double  decimal,
  4:string  name="thrifty"
}

exception ExampleException {
  1:i32     number=10,
  2:i64     big_number,
  3:double  decimal,
  4:string  name="thrifty"
}

service RemoteHashMap { 
    void          set(1:i32 key, 2:string value),
    string        get(1:i32 key) throws (1: KeyNotFound knf),
    async void delete(1:i32 key) 
}
