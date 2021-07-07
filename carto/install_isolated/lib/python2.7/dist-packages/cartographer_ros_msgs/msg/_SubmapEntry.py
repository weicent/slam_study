# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cartographer_ros_msgs/SubmapEntry.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class SubmapEntry(genpy.Message):
  _md5sum = "0b064ac06b4af2be11388441508c9572"
  _type = "cartographer_ros_msgs/SubmapEntry"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Copyright 2016 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

int32 trajectory_id
int32 submap_index
int32 submap_version
geometry_msgs/Pose pose
bool is_frozen

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['trajectory_id','submap_index','submap_version','pose','is_frozen']
  _slot_types = ['int32','int32','int32','geometry_msgs/Pose','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       trajectory_id,submap_index,submap_version,pose,is_frozen

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SubmapEntry, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.trajectory_id is None:
        self.trajectory_id = 0
      if self.submap_index is None:
        self.submap_index = 0
      if self.submap_version is None:
        self.submap_version = 0
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.is_frozen is None:
        self.is_frozen = False
    else:
      self.trajectory_id = 0
      self.submap_index = 0
      self.submap_version = 0
      self.pose = geometry_msgs.msg.Pose()
      self.is_frozen = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3i7dB().pack(_x.trajectory_id, _x.submap_index, _x.submap_version, _x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.is_frozen))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 69
      (_x.trajectory_id, _x.submap_index, _x.submap_version, _x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.is_frozen,) = _get_struct_3i7dB().unpack(str[start:end])
      self.is_frozen = bool(self.is_frozen)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3i7dB().pack(_x.trajectory_id, _x.submap_index, _x.submap_version, _x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.is_frozen))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 69
      (_x.trajectory_id, _x.submap_index, _x.submap_version, _x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.is_frozen,) = _get_struct_3i7dB().unpack(str[start:end])
      self.is_frozen = bool(self.is_frozen)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3i7dB = None
def _get_struct_3i7dB():
    global _struct_3i7dB
    if _struct_3i7dB is None:
        _struct_3i7dB = struct.Struct("<3i7dB")
    return _struct_3i7dB
