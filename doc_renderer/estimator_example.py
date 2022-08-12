from google.oauth2.credentials import Credentials

from doc_renderer.color import Color
from doc_renderer.doc_renderer import DocRenderer
from doc_renderer.paragraph_text_style import ParagraphTextStyle, ParagraphTextStyleEnum, ParagraphTextDecorationEnum
from doc_renderer.table_renderer import Row, Cell


def estimator_example_doc_renderer(credentials: Credentials):
    renderer = DocRenderer("2741 Youballin (Preliminary estimation)")
    renderer.create(credentials)

    renderer.add_text_line(
        text="Project ID: ",
        text_style=ParagraphTextStyle(
            font_size=12,
            decorations=[ParagraphTextDecorationEnum.BOLD],
        ),
        new_line=False,
    )

    renderer.add_text_line(
        text="2741",
        text_style=ParagraphTextStyle(
            font_size=12,
        ),
    )

    renderer.add_text_line(
        text="Date",
        text_style=ParagraphTextStyle(
            font_size=12,
            decorations=[ParagraphTextDecorationEnum.BOLD],
        ),
        new_line=False,
    )

    renderer.add_text_line(
        text=": 14/07/2022",
        text_style=ParagraphTextStyle(font_size=12),
    )

    renderer.add_text_line(
        text="To",
        text_style=ParagraphTextStyle(
            font_size=12,
            decorations=[ParagraphTextDecorationEnum.BOLD],
        ),
        new_line=False,
    )

    renderer.add_text_line(
        text=": Youballin",
        text_style=ParagraphTextStyle(font_size=12),
    )

    # Offer 2741: DEVELOPMENT OFFER
    renderer.add_table(
        rows=[
            Row(
                cells=[
                    Cell(
                        text="Offer 2741: DEVELOPMENT OFFER",
                        text_style=ParagraphTextStyle(
                            font_size=12,
                            decorations=[ParagraphTextDecorationEnum.BOLD],
                            font_color=Color.from_255(255, 255, 255),
                        ),
                        background_color=Color.from_255(50, 145, 230),
                    ),
                ]
            )
        ]
    )

    # Roles table
    header_style = ParagraphTextStyle(font_size=11, decorations=[ParagraphTextDecorationEnum.BOLD])
    cell_style = ParagraphTextStyle(font_size=11)
    renderer.add_table(
        rows=[
            Row(
                cells=[
                    Cell(
                        text="Role",
                        text_style=header_style,
                    ),
                    Cell(
                        text="People",
                        text_style=header_style,
                    ),
                    Cell(
                        text="Allocation, %",
                        text_style=header_style,
                    ),
                    Cell(
                        text="Period, months",
                        text_style=header_style,
                    ),
                    Cell(
                        text="Price per month, USD",
                        text_style=header_style,
                    ),
                    Cell(
                        text="Price, USD",
                        text_style=header_style,
                    ),
                ],
            ),
            Row(cells=[Cell(text="Senior Backend developer", text_style=cell_style)]),
            Row(cells=[Cell(text="Senior Frontend developer", text_style=cell_style)]),
            Row(cells=[Cell(text="Senior Blockchain developer", text_style=cell_style)]),
            Row(cells=[Cell(text="Project manager", text_style=cell_style)]),
            Row(cells=[Cell(text="QA Engineer", text_style=cell_style)]),
            Row(cells=[Cell(text="Tech lead", text_style=cell_style)]),
            Row(cells=[Cell(text="DevOps Engineer", text_style=cell_style)]),
            Row(cells=[Cell(text="Total", text_style=header_style)]),
        ]
    )

    # Note
    renderer.add_text_line(
        text="Note: ",
        text_style=ParagraphTextStyle(
            font_size=11,
            decorations=[ParagraphTextDecorationEnum.BOLD],
        ),
        new_line=False,
    )

    renderer.add_text_line(
        text="This is a high level pre-sale estimation which was done based on the analysis of Youballin’s whitepaper",
        text_style=ParagraphTextStyle(font_size=11),
    )

    # Deliverables
    renderer.add_text_line(
        text="Deliverables",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_2),
    )

    renderer.add_text_line(
        text="Key deliverables",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_unordered_list(
        lines=[
            "Development of the social media platform allowing interactions between the listed stakeholders as talents, fans, brands, etc",
            "Development of the Decentralized platform to perform play to earn competitions, voting options",
            "Development of the Local Token offering for the internal use",
            "Development of the Reputation Algorithm based on the Talent’s activity and related metadata such as likes, shared and flowers activity",
            "Project management, QA Testing and DevOps are included in the offer",
            "Detailed deliverables are listed in the Breakdowns section of this document",
        ],
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Deliverables",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_2),
    )

    renderer.add_text_line(
        text="Configured infrastructures (Test, Staging, Production)",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_unordered_list(
        lines=[
            "Backend application",
            "Frontend application",
            "Deployed smart contracts",
        ],
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Source code repository",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_unordered_list(
        lines=[
            "Backend application",
            "Frontend application",
            "Smart contracts",
        ],
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="CI/CD",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_unordered_list(
        lines=[
            "Container registry",
            "Configured CI and CD flow",
        ],
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Reports",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_unordered_list(
        lines=[
            "Work done",
            "Spent hours",
        ],
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Documentation",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_unordered_list(
        lines=[
            "API documentation",
            "Smart contracts documentation",
            "Deployment guide",
        ],
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Risks",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_2),
    )

    renderer.add_text_line(
        text="Stack",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_2),
    )

    renderer.add_text_line(
        text="Backend: Node.JS",
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Blockchain: EVM",
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="CI / CD: CD + GitHub",
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Actions",
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="for CI + DockerHub as a container registry",
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Cloud: AWS",
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Files: AWS",
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="S3, IPFS",
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Frontend: React.js",
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Logs: Sentry",
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Storage: Postgres + REDIS",
        text_style=ParagraphTextStyle(font_size=11),
    )

    # Breakdowns
    renderer.add_text_line(
        text="Breakdowns",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_2),
    )

    renderer.add_table(
        rows=[
            Row(
                cells=[
                    Cell(text="Scope", text_style=header_style),
                    Cell(text="Role", text_style=header_style),
                    Cell(text="Feature", text_style=header_style),
                ],
            ),
            Row(cells=[
                Cell(text="Backend", text_style=cell_style, merge_down=19),
                Cell(text="Backend developer", text_style=cell_style, merge_down=19),
                Cell(text="User management", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="NFT marketplace", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="NFT Minting", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="NFT Auctions", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="NFT Badge System (Ranking system)", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Streaming", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Video player/upload module", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Social Media", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Talents Dashboard", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Starts Dashboard", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Talent Agency, Media, and Ad Agencies Dashboard", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Fundraising module", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Voting module", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Merchandise store", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Event Processor", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Donations module", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Reputation algorithm", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Crypto wallet module", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Internal integrations", text_style=cell_style),
            ]),
            # next row
            Row(cells=[
                Cell(text="Frontend", text_style=cell_style, merge_down=19),
                Cell(text="Frontend developer", text_style=cell_style, merge_down=19),
                Cell(text="User management", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="NFT marketplace", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="NFT Minting", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="NFT Auctions", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="NFT Badge System (Ranking system)", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="DAO", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Streaming", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Video player/upload module", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Social Media", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Talents Dashboard", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Starts Dashboard", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Talent Agency, Media, and Ad Agencies Dashboard", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Fundraising module", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Voting module", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Merchandise store", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Event Processor", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Donations module", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Crypto wallet module", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Internal integrations", text_style=cell_style),
            ]),
            # next row
            Row(cells=[
                Cell(text="Blockchain", text_style=cell_style, merge_down=8),
                Cell(text="Blockchain developer", text_style=cell_style, merge_down=8),
                Cell(text="NFT marketplace", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="NFT Minting", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="NFT Auctions", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="NFT Badge System (Ranking system)", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="DAO", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Fundraising module", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Event Processor", text_style=cell_style),
            ]),
            Row(cells=[
                None,
                None,
                Cell(text="Internal integrations", text_style=cell_style),
            ]),
            # next row
            Row(cells=[
                Cell(text="Management", text_style=cell_style),
                Cell(text="Project manager", text_style=cell_style),
                Cell(text="Management", text_style=cell_style),
            ]),
            # next row
            Row(cells=[
                Cell(text="Quality Assurance", text_style=cell_style),
                Cell(text="QA Engineer", text_style=cell_style),
                Cell(text="Quality Assurance", text_style=cell_style),
            ]),
            # next row
            Row(cells=[
                Cell(text="Supervision", text_style=cell_style),
                Cell(text="Tech lead", text_style=cell_style),
                Cell(text="Supervision", text_style=cell_style),
            ]),
            # next row
            Row(cells=[
                Cell(text="Infrastructure", text_style=cell_style),
                Cell(text="DevOps Engineer", text_style=cell_style),
                Cell(text="Infrastructure", text_style=cell_style),
            ]),
            # next row
            Row(cells=[
                Cell(text="UI design", text_style=cell_style),
                Cell(text="UX designer", text_style=cell_style),
                Cell(text="UI design", text_style=cell_style),
            ]),
        ]
    )

    # Next stage:
    renderer.add_text_line(
        text="Next stage:",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_2),
    )

    renderer.add_text_line(
        text="Discovery recommended",
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Payment terms: 100% prepayment for each month.",
        text_style=ParagraphTextStyle(font_size=11),
    )

    renderer.add_text_line(
        text="Timelines: 3-4 weeks",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_text_line(
        text="Payment terms: 100% prepayment",
        text_style=ParagraphTextStyle(font_size=12),
    )

    renderer.add_text_line(
        text="Approach on Discovery Phase: Fixed Price",
        text_style=ParagraphTextStyle(font_size=12),
    )

    renderer.add_text_line(
        text="",
        text_style=ParagraphTextStyle(font_size=12),
    )

    renderer.add_text_line(
        text="* Optional (we recommend adding Designer services if you do not have your own. Designer will provide "
             "you with the UI Design Wireframes on the project).",
        text_style=ParagraphTextStyle(font_size=12),
    )

    renderer.add_text_line(
        text="Communication & Reporting",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_text_line(
        text="A Checkpoint call at least once a week, providing the progress and time reporting. Since this phase "
             "requires close collaboration with the Customer, Project Manager could initiate the kick-off meeting for "
             "several hours.",
        text_style=ParagraphTextStyle(font_size=12),
    )

    renderer.add_text_line(
        text="Benefits for starting the project with the proper Discovery Phase",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_list(
        lines=[
            "Identified risks and dependencies",
            "Aligning blockchain with the product needs",
            "Ready Proof-of-Concept as an interactive prototype in Invision",
            "Cost savings",
            "More precise estimates and plan",
            "Better fit customers needs",
        ],
        text_style=ParagraphTextStyle(font_size=12),
    )

    renderer.add_text_line(
        text="Fundamental Goals of the Discovery Phase",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_unordered_list(
        lines=[
            "Define functionality",
            "Define architecture",
            "Define project timelines and team composition",
            "Estimate detailed project cost",
        ],
        text_style=ParagraphTextStyle(font_size=12),
    )

    renderer.add_text_line(
        text="Deliverables",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_unordered_list(
        lines=[
            "Clarification of tech specifications",
            "Detailed Solution Architecture design and clarification",
            "Technologies justification",
            "Features prioritization and finalization",
            "High-Level Architecture of the functional components",
            "Roadmap draft for the project development",
            "List of features and components that should be prioritized",
            "Precise Budget for the development",
            "User Flow UX",
        ],
        text_style=ParagraphTextStyle(font_size=12),
    )

    renderer.add_text_line(
        text="If there is uncertainty in project requirements, 4ire Labs recommends clients to engage with Discovery "
             "Phase. That should fill the gaps and produce all necessary artifacts for final (commitment) estimates. "
             "Discovery Phase is a natural phase of large and complex projects.",
        text_style=ParagraphTextStyle(font_size=12),
    )

    renderer.add_text_line(
        text="Process",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_list(
        lines=[
            "4ire Labs involves PM/BA and Solution Architect in the Discovery Phase.",
            "We schedule the kick-off call with the client:",
            "\tParticipants: Sales Representative, PM/BA, Solution Architect.",
            "\t\tGoal: Alignment of Client’s expectations/requirements with the Delivery Team.",
            "\tOutcome: A follow-up letter summarizing the call and points agreed.",
            "PM/BA and Solution Architect sync up on the next steps, agreeing on the deliverables to be prepared for "
            "the Discovery Phase overall and for the next Checkpoint in particular.",
            "PM/BA schedules a weekly Checkpoint Call, deliverables shared prior to the call (in the presentation "
            "format).",
            "\tParticipants: PM/BA, Solution Architect, Sales Representative (optional).",
            "\tGoal: to report intermediate results to the Client, clarify the Client’s expectations/requirements.",
            "\tOutcome: A follow-up letter.",
            "Between the calls, communication is maintained via Email/Slack. Additional calls could be scheduled if "
            "needed.",
            "PM/BA and Solution Architect finalize the deliverables.",
            "We schedule a final call - Delivery Call, and present our vision and deliverables to the client.",
            "If the client is willing to proceed further, we sign the Contract and agree on the start date for the "
            "Development Phase.",
        ],
        text_style=ParagraphTextStyle(font_size=12),
    )

    renderer.add_page_break()

    # About FireLabs
    renderer.add_table(
        rows=[
            Row(
                cells=[
                    Cell(
                        text="About FireLabs",
                        text_style=ParagraphTextStyle(
                            font_size=12,
                            decorations=[ParagraphTextDecorationEnum.BOLD],
                            font_color=Color.from_255(255, 255, 255),
                        ),
                        background_color=Color.from_255(50, 145, 230),
                    ),
                ]
            )
        ]
    )

    renderer.add_text_line(
        text="Working in the software development field since 2010, we’ve made a contribution to a great variety of "
             "projects of some of the biggest names in the world.",
        text_style=ParagraphTextStyle(font_size=11, font_family="Roboto"),
    )

    renderer.add_unordered_list(
        lines=[
            "10+ years in software development & consulting",
            "90+ in-house engineers",
            "2 product companies (Datrics, MobId) that enhance our offering in FinTech and DeFi",
            "2 delivery centers (Kyiv, Stockholm)",
            "12 clients with annual revenue > $1B",
            "250+ finished projects",
            "4 awards",
            "80+ allies in the FinTech network",
        ],
        text_style=ParagraphTextStyle(font_size=11, font_family="Roboto"),
    )

    renderer.add_text_line(
        text="Our contribution into blockchain community",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3, font_family="Roboto"),
    )

    renderer.add_unordered_list(
        lines=[
            "Teaching blockchain in Ukraine (launched 3 solidity courses and rust course)",
            "Building long-term partnership with leading blockchain companies (Near, Parity, Chromia)",
            "Providing white-label blockchain solutions",
            "Participation in Ethereum Magicians circles",
            "Developing Distributed Governance community in DGOV Foundation",
            "Developing materials for solution-architects more on GitBook",
            "Developing Ukraine blockchain developers community #buidlua (partners Consensys)",
        ],
        text_style=ParagraphTextStyle(font_size=11, font_family="Roboto"),
    )

    renderer.add_text_line(
        text="Our portfolio of blockchain projects delivered",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3, font_family="Roboto"),
    )

    renderer.add_unordered_list(
        lines=[
            "Aztec Protocol / https://aztec.network\n"
            "DeFi. An efficient zero-knowledge privacy protocol for financial products.",
            "Contractland / https://www.contractland.io\n"
            "Web3.0. The Liquidity Infrastructure of Web3.0. It builds the infrastructure to provide liquidity of tokenized assets across various blockchains through high performing multi-chain technology.",
            "Green Assets Wallet / https://greenassetswallet.org\n"
            "Impact. The blockchain-based platform for a transparent and efficient green debt market. Supported by SEB bank, government entities in Sweden and Germany.",
        ],
        text_style=ParagraphTextStyle(font_size=11, font_family="Roboto"),
    )

    renderer.add_text_line(
        text="Partnerships and collaborations",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3, font_family="Roboto"),
    )

    renderer.add_text_line(
        text="We are part of the Substrate Delivery Program organized by ",
        text_style=ParagraphTextStyle(font_size=11, font_family="Roboto"),
        new_line=False
    )

    renderer.add_text_line(
        text="Parity.",
        text_style=ParagraphTextStyle(
            font_size=11,
            font_family="Roboto",
            decorations=[ParagraphTextDecorationEnum.BOLD]
        ),
    )

    renderer.add_text_line(
        text="4ire Labs is the official integrator of Chromia blockchain by ",
        text_style=ParagraphTextStyle(font_size=11, font_family="Roboto"),
        new_line=False
    )

    renderer.add_text_line(
        text="ChromaWay.",
        text_style=ParagraphTextStyle(
            font_size=11,
            font_family="Roboto",
            decorations=[ParagraphTextDecorationEnum.BOLD]
        ),
    )

    renderer.add_text_line(
        text="4ireLabs is the official ",
        text_style=ParagraphTextStyle(font_size=11, font_family="Roboto"),
        new_line=False
    )

    renderer.add_text_line(
        text="NEAR ",
        text_style=ParagraphTextStyle(
            font_size=11,
            font_family="Roboto",
            decorations=[ParagraphTextDecorationEnum.BOLD]
        ),
        new_line=False
    )

    renderer.add_text_line(
        text="partner and integrator.",
        text_style=ParagraphTextStyle(font_size=11, font_family="Roboto"),
        new_line=False
    )

    renderer.save()

    renderer.get()
