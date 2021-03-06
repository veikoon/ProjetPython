import dash_core_components as dcc
import dash_html_components as html

from web.utils import nav


class Year:
    """The Year module creates a dashboard which displays the number of songs per release date.

    """

    def __get_songs_per_year(self, songs: dict) -> dict:
        """Creates a dictionary containing the number of songs per year.

        Parameters
        ----------
        songs:  dict
                The dictionary containing songs with their metadata.

        Returns
        -------
        dict
            A dictionary containing the number of songs per year.

        """
        songs_per_year = dict()

        for song in songs:
            if "release_date" in songs[song]:
                if songs[song]["release_date"] not in songs_per_year:
                    songs_per_year[songs[song]["release_date"]] = 0
                for year in songs_per_year:
                    if year == songs[song]["release_date"]:
                        songs_per_year[year] += 1
        return songs_per_year

    def get_layout(self, songs: dict) -> html.Div:
        """Creates dashboard layout.

        Parameters
        ----------
        songs:  dict
                The dictionary containing songs with their metadata.

        Returns
        -------
        html.Div
            A HTML division containing the dashboard.
        """
        songs_per_year = self.__get_songs_per_year(songs)

        # Create graph.
        graph= dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': list(songs_per_year.keys()), 'y': list(songs_per_year.values()), 'type': 'bar', 'name': 'SF'},
                ],
                'layout': {
                    'title': 'Number of songs per year'
                }
            }
        )
        # Group the whole layout in a single HTML division.
        layout_year = html.Div(
            children=[
                nav,
                graph,
            ]
        )

        return layout_year

