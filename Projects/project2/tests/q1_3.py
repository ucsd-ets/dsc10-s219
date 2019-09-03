test = {
  'name': 'Question 1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(most_departures,np.ndarray)
          True
          >>> isinstance(most_arrivals,np.ndarray)
          True
          >>> len(most_arrivals) == 20
          True
          >>> len(most_departures) == 20
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