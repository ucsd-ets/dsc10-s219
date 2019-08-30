test = {
  'name': 'Question 4_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(tailnum_mileage,Table)
          True
          >>> 'TailNum' in tailnum_mileage.labels
          True
          >>> 'mileage' in tailnum_mileage.labels
          True
          >>> isinstance(tailnum_mileage.column('TailNum').item(0),str)
          True
          >>> isinstance(tailnum_mileage.column('mileage').item(0),int)
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