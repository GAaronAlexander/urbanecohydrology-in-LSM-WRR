












!
! Trigonometric functions which deal with degrees, rather than radians:
!

real function sind(theta)
  implicit none
  real, intent(in) :: theta
  real, parameter :: pi = 3.141592653589
  real, parameter :: degran = pi/180.
  sind = sin(theta*degran)
end function sind

real function cosd(theta)
  implicit none
  real, intent(in) :: theta
  real, parameter :: pi = 3.141592653589
  real, parameter :: degran = pi/180.
  cosd = cos(theta*degran)
end function cosd

real function tand(theta)
  implicit none
  real, intent(in) :: theta
  real, parameter :: pi = 3.141592653589
  real, parameter :: degran = pi/180.
  tand = tan(theta*degran)
end function tand

real function atand(x)
  implicit none
  real, intent(in) :: x
  real, parameter :: pi = 3.141592653589
  real, parameter :: raddeg = 180./pi
  atand = atan(x)*raddeg
end function atand

real function atan2d(x,y)
  implicit none
  real, intent(in) :: x,y
  real, parameter :: pi = 3.141592653589
  real, parameter :: raddeg = 180./pi
  atan2d = atan2(x,y)*raddeg
end function atan2d

real function asind(x)
  implicit none
  real, intent(in) :: x
  real, parameter :: pi = 3.141592653589
  real, parameter :: raddeg = pi/180.
  asind = asin(x)*raddeg
end function asind

real function acosd(x)
  implicit none
  real, intent(in) :: x
  real, parameter :: pi = 3.141592653589
  real, parameter :: raddeg = pi/180.
  acosd = acos(x)*raddeg
end function acosd
