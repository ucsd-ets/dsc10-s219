test = {
  'name': 'Question 1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(airports_with_coords,Table)
          True
          >>> 'longitude' in airports_with_coords.labels
          True
          >>> 'latitude' in airports_with_coords.labels
          True
          >>> isinstance(airports_with_coords.column('longitude').item(0),float)
          True
          >>> isinstance(airports_with_coords.column('latitude').item(0),float)
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