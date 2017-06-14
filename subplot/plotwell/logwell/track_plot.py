from __future__ import print_function


def single_track(lt, dmax, dmin):
    '''Create a single track log
    plot to disply one log over a
    specified dept range.abs

    Takes a a log track (lt) as a
    positional argument.

    dmax and dmin provide the range
    to plot the log across, this will
    modify the vertical exageration
    (strech) of the plot.
    '''

    plot_range = dmax-dmin

    # Find if positive or negative values entered
    if plot_range > 0:
        # Positive
        positive = True
    elif plot_range < 0:
        # Negative
        positive = False
    else:
        # Somethings not right then
        print("What's going on here then")


