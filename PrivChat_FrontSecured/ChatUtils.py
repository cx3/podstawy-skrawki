from __future__ import annotations

from typing import Dict, List


class RoomUser:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def get_name(self):
        return self.name

    def __eq__(self, other: RoomUser or str) -> bool:
        if isinstance(other, RoomUser):
            return self.ip == other.ip
        if isinstance(other, str):
            return self.ip == other
        raise TypeError


class ChatRooms:
    rooms = Dict[str, List[RoomUser]]

    def __init__(self):
        self.rooms: Dict[str: List[RoomUser]] = dict()
        self.access: Dict[str: str] = dict()

    def room_exists(self, roomname: str) -> bool:
        return roomname in self.rooms

    def is_username_in_room(self, username: str or RoomUser, roomname: str) -> bool:
        name = username
        if isinstance(username, RoomUser):
            name = username.get_name()
        if roomname in self.rooms:
            for user in self.rooms[roomname]:
                if name == user.get_name():
                    return True
        return False

    def is_user_in_room(self, user: RoomUser, roomname: str) -> bool:
        if roomname in self.rooms:
            for next_user in self.rooms[roomname]:
                if user == next_user:
                    return True
        return False

    def is_ip_in_room(self, ip: str, roomname: str) -> bool:
        if roomname in self.rooms:
            for user in self.rooms[roomname]:
                if user == ip:
                    return True
        return False

    def list_rooms_where_ip(self, ip: RoomUser or str) -> List[str]:
        result = []
        for room in self.rooms:
            for user in self.rooms[room]:
                if ip == user:
                    result.append(room)
        return sorted(list(set(result)))

    def join_user_to_room(self, user: RoomUser, roomname: str, password: str) -> bool:
        if roomname not in self.rooms:
            self.rooms[roomname] = [user]
            self.access[roomname] = password
            return True

        if self.is_username_in_room(user.get_name(), roomname):
            return False

        if not self.is_user_in_room(user, roomname):
            if self.access[roomname] == password:
                self.rooms[roomname].append(user)
                return True

        return False

    def name_by_ip_in_room(self, roomname, ip) -> bool or str:
        if roomname in self.rooms:
            for user in self.rooms[roomname]:
                if ip == user:
                    return user.get_name()
        return False


def test1():
    rooms = ChatRooms()
    print(rooms.join_user_to_room(RoomUser("alex", "192.168.1.1"), "room1", "passwd"))
    print(rooms.join_user_to_room(RoomUser("alexx", "192.168.1.3"), "room1", "passwdx"))
    print(rooms.is_ip_in_room("192.168.1.1", "room11"))
    print(rooms.list_rooms_where_ip("192.168.1.1"))
    print(rooms.name_by_ip_in_room("room1", "192.168.1.1"))


if __name__ == "__main__":
    test1()