import pytest
from User import User

user = User("John", "john@email.com", "FDUI87")

def test_init_user():
  assert user.Name == "John"
  assert user.Email == "john@email.com"
  assert user.Drivers_license == "FDUI87"
  
def test_create_post(monkeypatch, capsys):
  input = iter(["Johns †i†le", "I Just joined OOPX"])
  monkeypatch.setattr("builtins.input", lambda _x: next(input))
  user.create_a_post()
  assert len(user.posts) == 1
  assert len(user.User_posts) == 1
  user.see_my_posts()
  out, err = capsys.readouterr()
  assert "Johns †i†le" in out
  
def test_delete_post(monkeypatch, capsys):
  input = iter([1])
  monkeypatch.setattr("builtins.input", lambda _x: next(input))
  user.delete_a_post()
  assert len(user.posts) == 0
  assert len(user.User_posts) == 0
  user.see_my_posts()
  out, err = capsys.readouterr()
  assert out == ""

user2 = User(**{"name":"Mike", "email":"mike@email.com", "drivers_license":"FDUI87"})
user3 = User(**{"name":"Zack", "email":"zack@email.com", "drivers_license":"FDUI87"})       
  
def test_see_all_posts(monkeypatch, capsys):
  assert len(user.posts) == 0
  assert len(user.User_posts) == 0
  user.see_all_posts()
  out, err = capsys.readouterr()
  assert "Post deleted successfully!" in out
  assert "You have no posts." in out

  input = iter(["Zack åttåck", "B1@ck H@t"])
  monkeypatch.setattr("builtins.input", lambda _x: next(input))
  user3.create_a_post()
  assert len(user3.User_posts) == 1
  assert len(user.posts) == 1
  input = iter(["Mikes πost", "OOPX Founder"])
  monkeypatch.setattr("builtins.input", lambda _x: next(input))
  user2.create_a_post()
  assert len(user2.User_posts) == 1
  assert len(user.posts) == 2
  input = iter(["Johns †i†le", "I Just joined OOPX"])
  monkeypatch.setattr("builtins.input", lambda _x: next(input))
  user.create_a_post()
  assert len(user2.User_posts) == 1
  assert len(user.posts) == 3


def test_see_my_posts(monkeypatch, capsys):
  assert len(user.posts) == 3
  assert len(user.User_posts) == 1
  input = iter(["Zack åttåck", "B1@ck H@t"])
  monkeypatch.setattr("builtins.input", lambda _x: next(input))
  user.create_a_post()
  assert len(user.User_posts) == 2
  assert len(user.posts) == 4
  input = iter(["Mikes πost", "OOPX Founder"])
  monkeypatch.setattr("builtins.input", lambda _x: next(input))
  user.create_a_post()
  assert len(user.User_posts) == 3
  assert len(user.posts) == 5
  input = iter(["Johns †i†le", "I Just joined OOPX"])
  monkeypatch.setattr("builtins.input", lambda _x: next(input))
  user.create_a_post()
  assert len(user.User_posts) == 4
  assert len(user.posts) == 6