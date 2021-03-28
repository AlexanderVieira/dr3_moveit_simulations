# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from moveit_msgs/CollisionObject.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import object_recognition_msgs.msg
import shape_msgs.msg
import std_msgs.msg

class CollisionObject(genpy.Message):
  _md5sum = "dbba710596087da521c07564160dfccb"
  _type = "moveit_msgs/CollisionObject"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# A header, used for interpreting the poses
Header header

# DISCLAIMER: This field is not in use yet and all other poses
# are still interpreted in the header frame.
# https://github.com/ros-planning/moveit/pull/2037
# implements the actual logic for this field.
# ---
# The object's pose relative to the header frame.
# The shapes and subframe poses are defined relative to this pose.
geometry_msgs/Pose pose

# The id of the object (name used in MoveIt)
string id

# The object type in a database of known objects
object_recognition_msgs/ObjectType type

# The collision geometries associated with the object.
# Their poses are with respect to the object's pose

# Solid geometric primitives
shape_msgs/SolidPrimitive[] primitives
geometry_msgs/Pose[] primitive_poses

# Meshes
shape_msgs/Mesh[] meshes
geometry_msgs/Pose[] mesh_poses

# Bounding planes (equation is specified, but the plane can be oriented using an additional pose)
shape_msgs/Plane[] planes
geometry_msgs/Pose[] plane_poses

# Named subframes on the object. Use these to define points of interest on the object that you want
# to plan with (e.g. "tip", "spout", "handle"). The id of the object will be prepended to the subframe.
# If an object with the id "screwdriver" and a subframe "tip" is in the scene, you can use the frame
# "screwdriver/tip" for planning.
# The length of the subframe_names and subframe_poses has to be identical.
string[] subframe_names
geometry_msgs/Pose[] subframe_poses

# Adds the object to the planning scene. If the object previously existed, it is replaced.
byte ADD=0

# Removes the object from the environment entirely (everything that matches the specified id)
byte REMOVE=1

# Append to an object that already exists in the planning scene. If the object does not exist, it is added.
byte APPEND=2

# If an object already exists in the scene, new poses can be sent (the geometry arrays must be left empty)
# if solely moving the object is desired
byte MOVE=3

# Operation to be performed
byte operation

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

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

================================================================================
MSG: object_recognition_msgs/ObjectType
################################################## OBJECT ID #########################################################

# Contains information about the type of a found object. Those two sets of parameters together uniquely define an
# object

# The key of the found object: the unique identifier in the given db
string key

# The db parameters stored as a JSON/compressed YAML string. An object id does not make sense without the corresponding
# database. E.g., in object_recognition, it can look like: "{'type':'CouchDB', 'root':'http://localhost'}"
# There is no conventional format for those parameters and it's nice to keep that flexibility.
# The object_recognition_core as a generic DB type that can read those fields
# Current examples:
# For CouchDB:
#   type: 'CouchDB'
#   root: 'http://localhost:5984'
#   collection: 'object_recognition'
# For SQL household database:
#   type: 'SqlHousehold'
#   host: 'wgs36'
#   port: 5432
#   user: 'willow'
#   password: 'willow'
#   name: 'household_objects'
#   module: 'tabletop'
string db

================================================================================
MSG: shape_msgs/SolidPrimitive
# Define box, sphere, cylinder, cone 
# All shapes are defined to have their bounding boxes centered around 0,0,0.

uint8 BOX=1
uint8 SPHERE=2
uint8 CYLINDER=3
uint8 CONE=4

# The type of the shape
uint8 type


# The dimensions of the shape
float64[] dimensions

# The meaning of the shape dimensions: each constant defines the index in the 'dimensions' array

# For the BOX type, the X, Y, and Z dimensions are the length of the corresponding
# sides of the box.
uint8 BOX_X=0
uint8 BOX_Y=1
uint8 BOX_Z=2


# For the SPHERE type, only one component is used, and it gives the radius of
# the sphere.
uint8 SPHERE_RADIUS=0


# For the CYLINDER and CONE types, the center line is oriented along
# the Z axis.  Therefore the CYLINDER_HEIGHT (CONE_HEIGHT) component
# of dimensions gives the height of the cylinder (cone).  The
# CYLINDER_RADIUS (CONE_RADIUS) component of dimensions gives the
# radius of the base of the cylinder (cone).  Cone and cylinder
# primitives are defined to be circular. The tip of the cone is
# pointing up, along +Z axis.

uint8 CYLINDER_HEIGHT=0
uint8 CYLINDER_RADIUS=1

uint8 CONE_HEIGHT=0
uint8 CONE_RADIUS=1

================================================================================
MSG: shape_msgs/Mesh
# Definition of a mesh

# list of triangles; the index values refer to positions in vertices[]
MeshTriangle[] triangles

# the actual vertices that make up the mesh
geometry_msgs/Point[] vertices

================================================================================
MSG: shape_msgs/MeshTriangle
# Definition of a triangle's vertices
uint32[3] vertex_indices

================================================================================
MSG: shape_msgs/Plane
# Representation of a plane, using the plane equation ax + by + cz + d = 0

# a := coef[0]
# b := coef[1]
# c := coef[2]
# d := coef[3]

float64[4] coef
"""
  # Pseudo-constants
  ADD = 0
  REMOVE = 1
  APPEND = 2
  MOVE = 3

  __slots__ = ['header','pose','id','type','primitives','primitive_poses','meshes','mesh_poses','planes','plane_poses','subframe_names','subframe_poses','operation']
  _slot_types = ['std_msgs/Header','geometry_msgs/Pose','string','object_recognition_msgs/ObjectType','shape_msgs/SolidPrimitive[]','geometry_msgs/Pose[]','shape_msgs/Mesh[]','geometry_msgs/Pose[]','shape_msgs/Plane[]','geometry_msgs/Pose[]','string[]','geometry_msgs/Pose[]','byte']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,pose,id,type,primitives,primitive_poses,meshes,mesh_poses,planes,plane_poses,subframe_names,subframe_poses,operation

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CollisionObject, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.id is None:
        self.id = ''
      if self.type is None:
        self.type = object_recognition_msgs.msg.ObjectType()
      if self.primitives is None:
        self.primitives = []
      if self.primitive_poses is None:
        self.primitive_poses = []
      if self.meshes is None:
        self.meshes = []
      if self.mesh_poses is None:
        self.mesh_poses = []
      if self.planes is None:
        self.planes = []
      if self.plane_poses is None:
        self.plane_poses = []
      if self.subframe_names is None:
        self.subframe_names = []
      if self.subframe_poses is None:
        self.subframe_poses = []
      if self.operation is None:
        self.operation = 0
    else:
      self.header = std_msgs.msg.Header()
      self.pose = geometry_msgs.msg.Pose()
      self.id = ''
      self.type = object_recognition_msgs.msg.ObjectType()
      self.primitives = []
      self.primitive_poses = []
      self.meshes = []
      self.mesh_poses = []
      self.planes = []
      self.plane_poses = []
      self.subframe_names = []
      self.subframe_poses = []
      self.operation = 0

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w))
      _x = self.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.type.key
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.type.db
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.primitives)
      buff.write(_struct_I.pack(length))
      for val1 in self.primitives:
        _x = val1.type
        buff.write(_get_struct_B().pack(_x))
        length = len(val1.dimensions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.Struct(pattern).pack(*val1.dimensions))
      length = len(self.primitive_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.primitive_poses:
        _v1 = val1.position
        _x = _v1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v2 = val1.orientation
        _x = _v2
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.meshes)
      buff.write(_struct_I.pack(length))
      for val1 in self.meshes:
        length = len(val1.triangles)
        buff.write(_struct_I.pack(length))
        for val2 in val1.triangles:
          buff.write(_get_struct_3I().pack(*val2.vertex_indices))
        length = len(val1.vertices)
        buff.write(_struct_I.pack(length))
        for val2 in val1.vertices:
          _x = val2
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.mesh_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.mesh_poses:
        _v3 = val1.position
        _x = _v3
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v4 = val1.orientation
        _x = _v4
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.planes)
      buff.write(_struct_I.pack(length))
      for val1 in self.planes:
        buff.write(_get_struct_4d().pack(*val1.coef))
      length = len(self.plane_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.plane_poses:
        _v5 = val1.position
        _x = _v5
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v6 = val1.orientation
        _x = _v6
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.subframe_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.subframe_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.subframe_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.subframe_poses:
        _v7 = val1.position
        _x = _v7
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v8 = val1.orientation
        _x = _v8
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      _x = self.operation
      buff.write(_get_struct_b().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.type is None:
        self.type = object_recognition_msgs.msg.ObjectType()
      if self.primitives is None:
        self.primitives = None
      if self.primitive_poses is None:
        self.primitive_poses = None
      if self.meshes is None:
        self.meshes = None
      if self.mesh_poses is None:
        self.mesh_poses = None
      if self.planes is None:
        self.planes = None
      if self.plane_poses is None:
        self.plane_poses = None
      if self.subframe_poses is None:
        self.subframe_poses = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type.key = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.type.key = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type.db = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.type.db = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.primitives = []
      for i in range(0, length):
        val1 = shape_msgs.msg.SolidPrimitive()
        start = end
        end += 1
        (val1.type,) = _get_struct_B().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.dimensions = s.unpack(str[start:end])
        self.primitives.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.primitive_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v9 = val1.position
        _x = _v9
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v10 = val1.orientation
        _x = _v10
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.primitive_poses.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.meshes = []
      for i in range(0, length):
        val1 = shape_msgs.msg.Mesh()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.triangles = []
        for i in range(0, length):
          val2 = shape_msgs.msg.MeshTriangle()
          start = end
          end += 12
          val2.vertex_indices = _get_struct_3I().unpack(str[start:end])
          val1.triangles.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.vertices = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point()
          _x = val2
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.vertices.append(val2)
        self.meshes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mesh_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v11 = val1.position
        _x = _v11
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v12 = val1.orientation
        _x = _v12
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.mesh_poses.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.planes = []
      for i in range(0, length):
        val1 = shape_msgs.msg.Plane()
        start = end
        end += 32
        val1.coef = _get_struct_4d().unpack(str[start:end])
        self.planes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.plane_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v13 = val1.position
        _x = _v13
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v14 = val1.orientation
        _x = _v14
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.plane_poses.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.subframe_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.subframe_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.subframe_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v15 = val1.position
        _x = _v15
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v16 = val1.orientation
        _x = _v16
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.subframe_poses.append(val1)
      start = end
      end += 1
      (self.operation,) = _get_struct_b().unpack(str[start:end])
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w))
      _x = self.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.type.key
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.type.db
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.primitives)
      buff.write(_struct_I.pack(length))
      for val1 in self.primitives:
        _x = val1.type
        buff.write(_get_struct_B().pack(_x))
        length = len(val1.dimensions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.dimensions.tostring())
      length = len(self.primitive_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.primitive_poses:
        _v17 = val1.position
        _x = _v17
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v18 = val1.orientation
        _x = _v18
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.meshes)
      buff.write(_struct_I.pack(length))
      for val1 in self.meshes:
        length = len(val1.triangles)
        buff.write(_struct_I.pack(length))
        for val2 in val1.triangles:
          buff.write(val2.vertex_indices.tostring())
        length = len(val1.vertices)
        buff.write(_struct_I.pack(length))
        for val2 in val1.vertices:
          _x = val2
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.mesh_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.mesh_poses:
        _v19 = val1.position
        _x = _v19
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v20 = val1.orientation
        _x = _v20
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.planes)
      buff.write(_struct_I.pack(length))
      for val1 in self.planes:
        buff.write(val1.coef.tostring())
      length = len(self.plane_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.plane_poses:
        _v21 = val1.position
        _x = _v21
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v22 = val1.orientation
        _x = _v22
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.subframe_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.subframe_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.subframe_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.subframe_poses:
        _v23 = val1.position
        _x = _v23
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v24 = val1.orientation
        _x = _v24
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      _x = self.operation
      buff.write(_get_struct_b().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.type is None:
        self.type = object_recognition_msgs.msg.ObjectType()
      if self.primitives is None:
        self.primitives = None
      if self.primitive_poses is None:
        self.primitive_poses = None
      if self.meshes is None:
        self.meshes = None
      if self.mesh_poses is None:
        self.mesh_poses = None
      if self.planes is None:
        self.planes = None
      if self.plane_poses is None:
        self.plane_poses = None
      if self.subframe_poses is None:
        self.subframe_poses = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type.key = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.type.key = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type.db = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.type.db = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.primitives = []
      for i in range(0, length):
        val1 = shape_msgs.msg.SolidPrimitive()
        start = end
        end += 1
        (val1.type,) = _get_struct_B().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.dimensions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        self.primitives.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.primitive_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v25 = val1.position
        _x = _v25
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v26 = val1.orientation
        _x = _v26
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.primitive_poses.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.meshes = []
      for i in range(0, length):
        val1 = shape_msgs.msg.Mesh()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.triangles = []
        for i in range(0, length):
          val2 = shape_msgs.msg.MeshTriangle()
          start = end
          end += 12
          val2.vertex_indices = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=3)
          val1.triangles.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.vertices = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point()
          _x = val2
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.vertices.append(val2)
        self.meshes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mesh_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v27 = val1.position
        _x = _v27
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v28 = val1.orientation
        _x = _v28
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.mesh_poses.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.planes = []
      for i in range(0, length):
        val1 = shape_msgs.msg.Plane()
        start = end
        end += 32
        val1.coef = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=4)
        self.planes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.plane_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v29 = val1.position
        _x = _v29
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v30 = val1.orientation
        _x = _v30
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.plane_poses.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.subframe_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.subframe_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.subframe_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v31 = val1.position
        _x = _v31
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v32 = val1.orientation
        _x = _v32
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.subframe_poses.append(val1)
      start = end
      end += 1
      (self.operation,) = _get_struct_b().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_b = None
def _get_struct_b():
    global _struct_b
    if _struct_b is None:
        _struct_b = struct.Struct("<b")
    return _struct_b
