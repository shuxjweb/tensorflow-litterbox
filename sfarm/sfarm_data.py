#
"""StateFarm data set.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from fabric.dataset_record import DatasetRecord

class StateFarmData(DatasetRecord):
  """StateFarm data set."""

  def __init__(self, subset):
    super(StateFarmData, self).__init__('SFarm', subset)

  def num_examples_per_epoch(self):
    """Returns the number of examples in the data subset."""
    if self.subset == 'train':
      return 19328
    elif self.subset == 'validation':
      return 3096

  def num_classes(self):
    """Returns the number of classes in the data set."""
    return 10
