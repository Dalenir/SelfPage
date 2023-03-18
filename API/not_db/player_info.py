"""

Q: Why just not use sqllite?
A: I want my data easly accsessable to modification. I do not like using things in sake of using things.

"""
from not_db.summary import ssum, motivate


class PlayerData:

    PLs = {
        "Python": "About 1,5 years of commercial experience. Main instrument and duty at all my commercial orders and positions.",
        "JavaScript": "About 0,5 years of fragmentary expirience. Right now building a solid foundation.",
    }

    PythonSkills = {
        'Frameworks': [
            'Aiogram',
            'Django',
            'FastAPI',
            'Selenium',
            'SQLAlchemy',
            'Pytest'
        ],
        'Favorite libs': [
            'aiohttp',
            'pydantic',
            'psycopg2',
            'motor',
            'redis-py'
        ]
    }

    DevOpsSkills = {
        'Linux': 'I have extensive experience working with Linux and administering Linux-based systems. Currently, I am deepening my understanding of Linux through the "Linux & BSD" library by No Starch Press',
        'Docker': 'I use Docker for every project and can configure and manage swarm mode for container orchestration.',
        'Git': 'I use Git regularly for version control and/or collaboration.',
        'GitHub Actions': 'I have expertise in configuring CI/CD pipelines using GitHub Actions and integrating them with self-written notification apps for project boards.',
        'Grafana': 'I use Grafana to create dashboards for monitoring internal information and logs with Loki and Promtail.',
        'Ngnix': 'I have experience configuring Nginx and using it for simple load balancing and reverse proxy.',
        'Jenkins': 'I am skilled in configuring and managing Jenkins workers and creating declarative pipelines with email notifications.',
        'Ansible': 'I use Ansible for automating server initial configuration tasks. Mostly integrate it with Jenkins to automate routine processes.'
    }

    AQASkills = [
         "Strong understanding of test design principles and practices. Skilled in creating and maintaining test plans.",
         "Proficient in using Python to create, maintain, and debug automated tests. Capable of integrating them into CI pipelines.",
         "In-depth knowledge of application architecture, including front-end and back-end technologies.",
         "Experience working in collaborative environments using Agile methodologies such as Scrum and Kanban.",
         "Familiarity with testing tools and frameworks such as Selenium or Postman."
    ]

    TeamManagement = {
        'Achievements': [
            "Implemented Scrum methodology and now planning to obtain Scrum Master certification.",
            "Managed small teams using Kanban boards, effectively communicating with other project departments.",
            "Mentored colleagues, fostering their growth and professional development.",
            "Created and maintained internal documentation to ensure team understanding and knowledge retention.",
            "Motivated and inspired team members to achieve project success.",
            "Utilized technical expertise to effectively manage projects and make data-driven decisions to mitigate risks and ensure timely delivery."
        ],
        'Software': [
            'JetBrains Space',
            'Trello',
            'Clickup',
            'Notion',
            'Miro',
            'Jira'
        ]
    }

    notable = [
        'Networking',
        'Postman',
        'Blockchain',
        'SSH',
        'HTML/CSS'
    ]

    soft_skills = [
        'Teamwork',
        'Leadership',
        'Adaptability',
        'Problem Solving',
        'Fast Learning',
        'Technical Writing',
        'Communication',
        'Time Management',
        'Critical Thinking',
        'Emotional Intelligence',
        'Attention to Detail',
        'Mentorship',
        'Persistency'
    ]

    boring_stuff = """
    Let's save time:\n\nI grew up in corrupt state and saw effects of "small" deals on conscience. There is no invisible deals, no matter the size of man. I won't work for or help employer linked to dictatorial or corrupt gov. Prefer losing "unique chance" & money than getting involved in something karmically bad.\nYeah, funny, I know."""

    summary = ssum
    motivate = motivate