import pytest

from modules.book_analytics import BookAnalytics

def test_parse_book_content():
    ba = BookAnalytics("64317.txt.utf-8", book_path="tests/mocks")
    windows, title = ba.parse_windows()
    for window in windows:
        print([window])
    assert len(windows) == 7
    assert title == "The Great Gatsby"
    assert windows[2]['sentiment']['pos'] == 0.112
    
    # TODO: I should choose better and perhaps longer test corpus
    # to get some actual differentces to the ranks
    compound_rank = ba.rank_windows(windows, "compound")
    print(compound_rank)
    assert compound_rank[2]['para_id'] == 4
    mov_avg_rank = ba.rank_windows(windows, "mov_avg")
    print(mov_avg_rank)
    assert mov_avg_rank[2]['para_id'] == 2
    inter_sum_rank = ba.rank_windows(windows, "inter_sum")
    print(inter_sum_rank)
    assert inter_sum_rank[1]['para_id'] == 1
    
    
    