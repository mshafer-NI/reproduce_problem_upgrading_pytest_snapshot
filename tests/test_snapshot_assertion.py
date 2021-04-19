def test__given_multiline_string__snapshot_assert__should_pass(snapshot):
    multiline_string = "\n".join(["lorem", "ipsum", "dolor", "sit", "amet"])

    snapshot.assert_match(multiline_string, "multiline_string.txt")
