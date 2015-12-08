"""
Convenience module for access of custom tagging application settings,
which enforces default settings when the main settings module does not
contain the appropriate settings.
"""

# The maximum length of a tag's name.
DEFAULT_MAX_TAG_LENGTH = 50

# Whether to force all tags to lowercase before they are saved to the
# database.
DEFAULT_FORCE_LOWERCASE_TAGS = False
