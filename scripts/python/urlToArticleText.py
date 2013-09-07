
from goose import Goose

g = Goose()

# NOTE, on error this will return ''. Caller should check for this
# and not try to text-to-speech it.
print g.extract('http://rss.cnn.com/~r/rss/cnn_topstories/~3/-d862QE5E7U/index.html').cleaned_text

