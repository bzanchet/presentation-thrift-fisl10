namespace py example
namespace php example

enum MartialArt {
  AIKIDO    = 1,
  KARATE    = 2
}

struct UserProfile {
  1: i32            uid,
  2: string         name,
  3: MartialArt     style
}

service UserStorage {
  void          store(1: UserProfile user),
  UserProfile   retrieve(1: i32 uid)
}
