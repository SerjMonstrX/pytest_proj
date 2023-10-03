from utils import arrs, dicts


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert arrs.my_slice([]) == []

def test_get_val():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs" ) == "mercurial"
    assert dicts.get_val({"vcs": "mercurial"}, "vcs", 'git' ) == "mercurial"
    assert dicts.get_val({"vcsss": "mercurial"}, "vcs", ) == 'git'
    assert dicts.get_val({"vcsss": "mercurial"}, "vcs", 'bazaar') == 'bazaar'
    assert dicts.get_val({}, "vcs" ) == 'git'
    assert dicts.get_val({}, '') == 'git'
