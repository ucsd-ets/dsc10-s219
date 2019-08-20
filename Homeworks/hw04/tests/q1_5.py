test = {
  'name': 'Question 1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> callable(lastname_length)
          True
          >>> lastname_length('Quer, Giorgio') == "very short"
          True
          >>> lastname_length('Twomey, Robert') == "normal"
          True
          >>> lastname_length('Tiefenbruck, Janine') == "very long"
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
