test = {
  'name': 'Question 2_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # ===================================
          >>> # We are asking for a category !!!
          >>> # ===================================
          >>> isinstance(best_category, str)
          True
          >>> best_category in apps.column('Category')
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
