test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs(average_1900s_rating - 8.2783625730994146) < 1e-5
          True
          >>> abs(average_2000s_rating - 8.2379746835443033) < 1e-5
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
