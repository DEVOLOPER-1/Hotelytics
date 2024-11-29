from dash import dcc, html
from graphs import (
    BookingTrendsandCustomerBehavior as BTCB,
    CustomerDemographicsandPreferences as CDP,
)
import dash_bootstrap_components as dbc
from PIL import Image

# from dash_bootstrap_templates import ThemeSwitchAIO

# theme_switch = ThemeSwitchAIO(
#     aio_id="theme", themes=[dbc.themes.COSMO, dbc.themes.CYBORG]
# )

read_image = Image.open(r"Assets\idv5FeoEqU_1731534349237.png")


layout = html.Div(
    [
        dbc.Container(
            # html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.CardLink(
                                href="https://intercontinentalsemiramis.com-cairo.com/",
                                children=[
                                    html.Img(
                                        src=read_image,
                                        width=150,
                                        height=150,
                                    )
                                ],
                                external_link=True,
                                target="_blank",
                            ),
                            width=2,
                            align="left",
                        ),
                        dbc.Col(
                            [
                                html.H1(
                                    "InterContinental Cairo Semiramis Hotel - Analytics 📊"
                                )
                            ],
                            width=11,
                        ),
                        # dbc.Col(theme_switch, width="auto"),  # Theme switch positioned beside title
                    ],
                    align="center",
                    justify="center",
                ),
                dbc.Tabs(
                    id="tabs_container",
                    children=[
                        dbc.Tab(
                            label="Booking Trends and Customer Behavior",
                            children=[
                                dbc.Card(
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dcc.Graph(
                                                    figure=BTCB.cancelation_trends_per_season()
                                                ),
                                                width=6,
                                            ),
                                            dbc.Col(
                                                dcc.Graph(
                                                    figure=BTCB.Cancellations_vs_guests_types()
                                                ),
                                                width=6,
                                            ),
                                        ],
                                        align="center",
                                    )
                                ),
                                dbc.Card(
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dcc.Graph(
                                                    figure=BTCB.cancellations_vs_market_segment()
                                                )
                                            ),
                                            dbc.Col(
                                                dcc.Graph(
                                                    figure=BTCB.lead_times_per_hotel()
                                                )
                                            ),
                                            dbc.Col(
                                                dcc.Graph(
                                                    figure=BTCB.relation_of_requests_vs_cancellations()
                                                )
                                            ),
                                        ]
                                    )
                                ),
                                dbc.Card(
                                    children=[
                                        dbc.Row(
                                            children=[
                                                dbc.Col(
                                                    dcc.Graph(
                                                        id="Cancelation_trands_graph",
                                                        figure=BTCB.cancellations_trends_graph(),
                                                    ),
                                                ),
                                                dbc.Container(
                                                    children=[
                                                        dbc.Card(
                                                            children=[
                                                                dcc.Slider(
                                                                    id="YearSlider",
                                                                    min=2015,
                                                                    max=2017,
                                                                    step=1,
                                                                    included=False,
                                                                    marks={
                                                                        2015: "2015",
                                                                        2016: "2016",
                                                                        2017: "2017",
                                                                    },
                                                                    tooltip={
                                                                        "placement": "bottom",
                                                                        "always_visible": False,
                                                                    },
                                                                    value=2017,
                                                                )
                                                            ],
                                                        ),
                                                        dbc.Card(
                                                            children=[
                                                                dcc.Slider(
                                                                    id="MonthSlider",
                                                                    min=1,
                                                                    max=12,
                                                                    step=1,
                                                                    included=False,
                                                                    tooltip={
                                                                        "placement": "top",
                                                                        "always_visible": False,
                                                                    },
                                                                    value=12,
                                                                )
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ]
                                        )
                                    ]
                                ),
                            ],
                        ),
                        dbc.Tab(
                            label="Customer Demographics and Preferences",
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            dcc.Graph(
                                                figure=CDP.average_stay_per_hotels()
                                            ),
                                            width=6,
                                        ),
                                        dbc.Col(
                                            dcc.Graph(
                                                figure=CDP.frequent_reserved_and_assigned_rooms()
                                            ),
                                            width=6,
                                        ),
                                    ],
                                    align="center",
                                ),
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            dcc.Graph(
                                                figure=CDP.relation_of_cancelation_rates_and_siblings()
                                            ),
                                            width=6,
                                        ),
                                        dbc.Col(
                                            dcc.Graph(
                                                figure=CDP.types_of_customers_vs_requiring_parking_rates()
                                            ),
                                            width=6,
                                        ),
                                    ],
                                    align="center",
                                ),
                                dbc.Row(
                                    dcc.Graph(figure=CDP.meal_prefrences_vs_countries())
                                ),
                            ],
                        ),
                    ],
                    className="nav-justified",
                ),
                # dbc.Input(id="input-field", type="text", placeholder="Enter something..."),
                # html.Div(id="output-div", style={"margin-top": "20px"}),
                # html.Div(
                #     dbc.Pagination(
                #         id="navigation_through_tabs",
                #         max_value=2,
                #         first_last=2,
                #         previous_next=True,
                #     )
                # ),
            ]
            # )
        ),
    ]
)
