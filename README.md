# Summary<a id="orgheadline1"></a>

General software for managing trajectories and the interface with
TrueBeam's Developer Mode. Most of the functionality of the code,
classes, and methods are tracked within the docstrings of the
code. This file is mainly to keep track of the overall code design and
ideas that remain to be implemented.

# TODO UML<a id="orgheadline20"></a>

As the object oriented nature of this project would benefit from good
design, I will use this to both learn how to implement UML using the
4+1 design method.

## TODO Use Cases<a id="orgheadline19"></a>

-   Heart of the design that affects all other aspects of the
    software. This is the level that describes the requirements
    of the end user.
-   Priority is assigned to determine which parts of the code that
    should be developed first.
-   The use cases should define what the system should do.

### Requirements<a id="orgheadline17"></a>

Here the requirements are broken into major categories and assigned
priority.

1.  A. Parametric trajectory

    The code shall generate a list of the view locations for different
    scanning trajectories.

    1.  DONE A.1 Create a trajectory

        -   The package shall allow the user to generate a scanning trajectory
            based on a series of control points.

        -   [ ] The trajectory should be defined as a continuous piecewise
            function of time.

        -   These rate of change for the components of these sections should be
            calculated from the limiting velocities of the physical system.

        1.  TODO Fix piecewise code

            -   [ ] Currently bug in SymPy code for evaluating multiple piecewise
                conditions. In discussion with SymPy team to rectify this.

    2.  TODO A.2 Generate view locations

        -   Given the continuous piecewise function of the trajectory, the
            package shall sample trajectory positions based on the specified
            frame rate.

        -   At these sampled time points, the package should generate a frame
            vector for the source and detector.

    3.  DONE A.3 Load a trajectory

        -   Given a list of frame vectors, the package should be able to
            initialize an instance of the trajectory object.

    4.  TODO Wish list

        -   [ ] Direct frame vector access from within the reconstruction scripts
            would be useful&#x2026;

2.  B. Trajectory visualization

    1.  DONE B.1 Plot source trajectory

        -   For a given trajectory, the package should be able to generate a 3D
            plot of the source position in space.

        -   It should also be able to generate plots along each basis of the
            trajectories position and velocity as a function of time. This
            should also include the angular information in addition to the
            spatial coordinates.

    2.  DONE B.2 Plot detector trajectory

        -   The package should have the exact same plotting capability for the
            detector center as the source.

    3.  TODO Wish list

        -   [ ] The package should also be able to plot the detector tilt along
            it's three degrees of freedom.

        -   [ ] Need to determine best way to represent relative motion around
            imaging isocenter in reconstruction. Currently only experimented
            with couch longitudinal translation and this relative translation is
            implemented as source and detector motion in the reconstruction.

3.  C. BeamXML interface

    1.  DONE C.1 Generate a beamxml file for a given trajectory

        -   The package shall be able to populate a beamxml file as a series of
            control points for imaging.

    2.  DONE C.2 Generate a trajectory from a beamxml file

        -   The package should be able to populate a trajectory based on the
            control in the beamxml file.

    3.  DONE C.3 Use beamxml schema to manage xml interface

    4.  TODO Wish list

        -   [ ] For detector offsets, make sure the collimator blades are
            correctly moved in the xml file as well.
            -   This is currently implemented via different initial configuration
                templates. This needs to be dynamically calculated.

            -   Dynamic blade motion will be necessary if shifting detector offset
                within the trajectory.

### TODO Descriptions<a id="orgheadline18"></a>

<table id="orgtable1" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Use case name</th>
<th scope="col" class="org-left">Create trajectory</th>
<th scope="col" class="org-left">&#xa0;</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Use case description</td>
<td class="org-left">Generates a trajectory of interest.</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Related Requirements</td>
<td class="org-left">A.1</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Goal in Context</td>
<td class="org-left">The code is designed for studying source and detector trajectories which this use case creates</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Preconditions</td>
<td class="org-left">A list of control points must be given that describe the trajectory.</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Successful End Condition</td>
<td class="org-left">A trajectory object should be created.</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Failed End Condition</td>
<td class="org-left">No trajectory is created and user is alerted</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Primary Actors</td>
<td class="org-left">User</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Secondary Actors</td>
<td class="org-left">Load frame vectors</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">Load beamxml</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Trigger</td>
<td class="org-left">Initialize new trajectory object</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Included Cases</td>
<td class="org-left">Create coordinate system.</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Main Flow</td>
<td class="org-left">Step</td>
<td class="org-left">Action</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">1.</td>
<td class="org-left">Load control points</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">2.</td>
<td class="org-left">Create symbolic piecewise function based on limiting velocities</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">3.</td>
<td class="org-left">Calculate frame vectors</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Extension</td>
<td class="org-left">Step</td>
<td class="org-left">Branching Action</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">3.1</td>
<td class="org-left">Populate frame vectors with detector tilt if specified.</td>
</tr>
</tbody>
</table>

<table id="orgtable2" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Use case name</th>
<th scope="col" class="org-left">Plot trajectory</th>
<th scope="col" class="org-left">&#xa0;</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Use case description</td>
<td class="org-left">Creates a plot of a given trajectory</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Related Requirements</td>
<td class="org-left">B.1</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Goal in Context</td>
<td class="org-left">Visualize the trajectory of the trajectory object</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Preconditions</td>
<td class="org-left">Trajectory must be successfully created</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Successful End Condition</td>
<td class="org-left">Plot object should be created</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Failed End Condition</td>
<td class="org-left">No plot should be generated and the user should be alerted</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Primary Actors</td>
<td class="org-left">User</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Secondary Actors</td>
<td class="org-left">None</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Trigger</td>
<td class="org-left">User requests a trajectory plot</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Included Cases</td>
<td class="org-left">None</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Main Flow</td>
<td class="org-left">Step</td>
<td class="org-left">Action</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">1.</td>
<td class="org-left">Initialize the plotting environment</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">2.</td>
<td class="org-left">Plot the trajectory in the 3D coordinate system</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Extension</td>
<td class="org-left">Step</td>
<td class="org-left">Branching Action</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">1.1</td>
<td class="org-left">Generate 2D plot of selected components</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">2.1</td>
<td class="org-left">Write plot to file.</td>
</tr>
</tbody>
</table>