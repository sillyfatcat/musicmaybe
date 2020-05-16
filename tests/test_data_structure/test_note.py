from musicmaybe.models import Note


class TestNotes:
    def test_note_data_structure_create(self):
        n = Note('C', 1.0, ('sharp',))
        assert n.note == 'C'
        assert n.beat == 1
        assert n.modifier == 'sharp'

    def test_note_beyond_range(self):
        n = Note('Z', 1, ('sharp',))
        assert n is None

    def test_note_length_modifier(self):
        n = Note('C', 1.0, ('dotted',))
        assert n.note == 'C'
        assert n.beat == 1.5
        assert n.modifiers == ('dotted',)

    def test_note_length_modifier_and_pitch(self):
        n = Note('C', 2, ('flat', 'dotted',))
        assert n.note == 'C'
        assert n.beat == 3
        assert n.modifiers == ('flat', 'dotted',)

    def test_note_rest(self):
        n = Note('-', 2, ())
        assert n.note == '-'
        assert n.beat == '2'
        assert n.modifiers == ()
