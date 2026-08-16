# Email Simulator (email_simulator.py)

A Python simulation of a basic email system, with `User`, `Inbox`, and `Email` classes that let users send, receive, read, and delete emails from each other's inboxes.

## Features

- Create `User` objects, each with their own `Inbox`
- Send emails between users, automatically delivered to the receiver's inbox
- List all emails in an inbox with read/unread status
- Read a specific email, which marks it as read and prints full details (sender, receiver, subject, timestamp, body)
- Delete a specific email from an inbox
- Timestamps are automatically recorded when an email is created

## Requirements

- Python 3.6+ (uses f-strings, `datetime` from the standard library)
- No external dependencies

## Usage

```python
from email_simulator import User

tory = User('Tory')
ramy = User('Ramy')

tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')

ramy.check_inbox()
ramy.read_email(1)
ramy.delete_email(1)
ramy.check_inbox()
```

Running the file directly (`python email_simulator.py`) executes this exact demo via the built-in `main()` function.

### Example output

```
Email sent from Tory to Ramy!

Email sent from Ramy to Tory!


Ramy's Inbox:

Your Emails:
1. [Unread] From: Tory | Subject: Hello | Time: 2026-08-16 10:32

--- Email ---
From: Tory
To: Ramy
Subject: Hello
Received: 2026-08-16 10:32
Body: Hi Ramy, just saying hello!
------------

Email deleted.


Ramy's Inbox:
Your inbox is empty.
```

## Classes

### `User`

| Method | Description |
|---|---|
| `__init__(name)` | Creates a user with a `name` and a fresh, empty `Inbox`. |
| `send_email(receiver, subject, body)` | Creates an `Email` from this user and delivers it to `receiver`'s inbox. |
| `check_inbox()` | Prints a numbered list of all emails in this user's inbox. |
| `read_email(index)` | Displays the full contents of the email at position `index` (1-based) and marks it as read. |
| `delete_email(index)` | Deletes the email at position `index` (1-based). |

### `Inbox`

| Method | Description |
|---|---|
| `__init__()` | Creates an empty inbox (`emails` list). |
| `receive_email(email)` | Appends an `Email` object to the inbox. |
| `list_emails()` | Prints all emails with their index, or a message if the inbox is empty. |
| `read_email(index)` | Validates the index and displays the corresponding email in full. |
| `delete_email(index)` | Validates the index and removes the corresponding email. |

### `Email`

| Member | Description |
|---|---|
| `__init__(sender, receiver, subject, body)` | Creates an email; automatically sets `timestamp` to the current time and `read` to `False`. |
| `mark_as_read()` | Sets `self.read = True`. |
| `display_full_email()` | Marks the email as read and prints all its details (sender, receiver, subject, timestamp, body). |
| `__str__()` | Returns a one-line summary: `[Read/Unread] From: <sender> | Subject: <subject> | Time: <timestamp>`. |

## Notes / Limitations

- Indexing for `read_email` and `delete_email` is **1-based**, not 0-based — user-facing convenience, but easy to trip over if calling these methods directly.
- Emails are stored only in memory; nothing is persisted to a file or database, so all mail is lost when the program ends.
- `sender` and `receiver` are expected to be `User` objects (their `.name` attribute is accessed directly) — passing a plain string will raise an `AttributeError`.
- There's no validation on `subject` or `body` — empty strings or unusual types are accepted without error.
- Deleting an email shifts the indices of all emails after it, so repeatedly deleting by a stored index without refreshing the list could target the wrong email.
