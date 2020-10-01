#!/usr/bin/env python

# This simple example shows how to do basic rendering and pipeline
# creation.

import sys
import vtk

# The colors module defines various useful colors.
from vtk.util.colors import tomato
from vtk.util.colors import blue

# This creates a polygonal mesh from an STL
stlReader = vtk.vtkSTLReader()
stlReader.SetFileName('cerebelum.stl')

# reverse the winding of the polygons
stlReverse = vtk.vtkReverseSense()
stlReverse.SetInputConnection(stlReader.GetOutputPort())
stlReverse.Update()

# remove holes from inside
stlConnectivity = vtk.vtkConnectivityFilter()
#stlConnectivity.SetInputConnection(stlReverse.GetOutputPort())
stlConnectivity.SetInputConnection(stlReader.GetOutputPort())
stlConnectivity.SetExtractionModeToLargestRegion()
stlConnectivity.Update()

# write to a new STL file
stlWriter = vtk.vtkSTLWriter()
stlWriter.SetInputConnection(stlConnectivity.GetOutputPort())
stlWriter.SetFileName('cerebelumNew.stl')
stlWriter.Write()

# The mapper is responsible for pushing the geometry into the graphics
# library. It may also do color mapping, if scalars or other
# attributes are defined.
stlMapper = vtk.vtkPolyDataMapper()
stlMapper.SetInputConnection(stlConnectivity.GetOutputPort())

# The actor is a grouping mechanism: besides the geometry (mapper), it
# also has a property, transformation matrix, and/or texture map.
# Here we set its color and rotate it -22.5 degrees.
stlActor = vtk.vtkActor()
stlActor.SetMapper(stlMapper)
stlActor.GetProperty().SetColor(tomato)
#stlActor.SetBackfaceProperty(vtk.vtkProperty())
#stlActor.GetBackfaceProperty().SetColor(blue)
stlActor.GetProperty().SetOpacity(0.5)
stlActor.RotateX(30.0)
stlActor.RotateY(-45.0)

# Create the graphics structure. The renderer renders into the render
# window. The render window interactor captures mouse events and will
# perform appropriate camera or actor manipulation depending on the
# nature of the events.
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Add the actors to the renderer, set the background and size
ren.AddActor(stlActor)
ren.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(1000, 1000)

# This allows the interactor to initalize itself. It has to be
# called before an event loop.
iren.Initialize()

# We'll zoom in a little by accessing the camera and invoking a "Zoom"
# method on it.
ren.ResetCamera()
ren.GetActiveCamera().Zoom(1.5)
renWin.Render()

# Start the event loop.
print('Running')
iren.Start()
