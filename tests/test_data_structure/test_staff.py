from musicmaybe.models import (
    Note,
    Staff,
)


class TestStaff:
    def test_creating_staff_with_notes(self):
        notes = [
            Note('C', 1, ()),
            Note('B', 2, ()),
            Note('C', 1, ('sharp', )),
        ]
        s = Staff(notes)
        assert notes == s.notes
        assert 4 == s.duration

    def test_creating_staff_with_combination_of_notes_and_rests(self):
        notes = [
            Note('-', 2, ()),
            Note('C', 1, ('sharp',)),
        ]
        s = Staff(notes)
        assert notes == s.notes
        assert 3 == s.duration
