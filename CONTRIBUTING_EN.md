# 🌟 Contributing Guide

**[中文](CONTRIBUTING.md)** | **[English](CONTRIBUTING_EN.md)**

Welcome to the Public Meteorological Data repository! Thank you for your willingness to contribute to this project. This guide will help you understand how to make contributions.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
  - [Reporting Issues](#reporting-issues)
  - [Adding New Data Sources](#adding-new-data-sources)
  - [Improving Documentation](#improving-documentation)
  - [Submitting Code](#submitting-code)
- [Contribution Workflow](#contribution-workflow)
- [Data Source Standards](#data-source-standards)
- [Documentation Standards](#documentation-standards)
- [Code Standards](#code-standards)
- [Review Process](#review-process)
- [Community](#community)

## Code of Conduct

When participating in this project, please follow our code of conduct:

- 🤝 **Be Respectful**: Maintain a friendly and professional communication atmosphere
- 📚 **Be Helpful**: Help new members get familiar with the project
- 🔍 **Be Rigorous**: Ensure that submitted data is accurate and reliable
- 📄 **Respect Agreements**: Respect the terms of use of data providers
- 🌐 **Be Inclusive**: Welcome contributors from diverse backgrounds

## How to Contribute

### Reporting Issues

If you find any of the following issues, please report them via the [Issues](../../issues) page:

- 🔗 **Broken Links**: Data links that are inaccessible
- 📊 **Outdated Information**: Data source information that needs updating
- ❌ **Data Errors**: Incorrect data descriptions or classifications
- 💡 **Feature Suggestions**: Suggestions for project improvement
- ➕ **Resource Recommendations**: Recommendations for new data sources

**Issue Report Template:**
```markdown
## Issue Type
[ ] Broken Link [ ] Outdated Info [ ] Data Error [ ] Feature Suggestion [ ] Resource Recommendation

## Description
<!-- Describe the issue in detail -->

## Affected Section
<!-- If it's a broken link or data error, please specify the exact location -->

## Suggested Solution (Optional)
<!-- If you have a suggested solution, please describe it here -->

## Environment Info
- OS:
- Browser:
- Date discovered:
```

### Adding New Data Sources

When adding a new data source, please ensure:

1. **Publicly Accessible**: Can be accessed without registration or payment
2. **Reliable Source**: From an official or well-known institution
3. **Standard Format**: Added following the existing categories and collapsible card format
4. **Complete Information**: Includes all required badges and links

**Data Source Addition Template:**

```markdown
<details>
<summary><b>Data Name</b> · Institution / Brief description</summary>

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~384h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Data_Provider-color_code?style=flat-square)

🔗 [Data Link](https://example.com/data) · 📅 Data Period · 📝 [Example Code](./sources/example.py)

</details>
```

**Badge Color Standards:**

| Source Type | Color Code | Examples |
|-------------|------------|----------|
| Official Agencies | `9CF` | CMA, DWD, JMA |
| NOAA | `00CED1` | NOAA, NCEP |
| NASA | `FF0000` | NASA, MERRA-2 |
| UCAR | `800080` | UCAR, NCAR |
| ECMWF/CDS | `00CED1` | ECMWF, CDS |
| ESA/Copernicus | `003399` | ESA, Copernicus |
| AWS | `FF9900` | AWS S3 |
| Google | `4285F4` | Google Cloud |
| OpeNDAP | `00BFFF` | OpeNDAP Services |
| Other | `00BFFF` | Other data providers |

**Badge Field Descriptions:**

| Badge | Purpose | Applicable Data Types |
|-------|---------|----------------------|
| Resolution | Spatial resolution | Gridded data |
| Range | Forecast range | Forecast data |
| Update | Data update frequency | All data |
| Source | Data provider | All data |
| Time Resolution | Time interval | Reanalysis/observation data |
| Time Range | Historical data coverage | Historical data |
| Magic | Requires special network | Requires VPN access |
| Type | Data type | Climate/observation data |

### Improving Documentation

We welcome improvements to the project documentation, including:

- ✏️ **Fixing typos and grammar errors**
- 🎨 **Improving document structure and readability**
- 🔧 **Enhancing usage instructions and examples**
- 🌍 **Adding multi-language translations**

### Submitting Code

If you have programming skills, you can contribute:

- 🛠️ **Data processing scripts**
- 📊 **Data validation tools**
- 🔗 **API wrapper libraries**
- 🧪 **Test cases**

## Contribution Workflow

### 1. Fork the Repository

1. Click the "Fork" button in the top right corner of the GitHub page
2. Clone the project locally:
```bash
git clone https://github.com/wait4xx/Meteorological-Data-Download-Guide.git
cd Meteorological-Data-Download-Guide
```

### 2. Create a Branch

Create a feature branch for your contribution:
```bash
git checkout -b feature/your-feature-name
```
Branch naming conventions:
- `feature/data-source-name` - Adding a new data source
- `fix/issue-description` - Fixing an issue
- `docs/topic` - Documentation improvement

### 3. Make Changes

Make your changes locally, ensuring:
- Follow the project's code and documentation standards
- Test the validity of all links
- Update related documentation

### 4. Commit Changes

Use descriptive commit messages:
```bash
git add .
git commit -m "feat: add China Meteorological Administration global model data source"
```

Commit message format:
- `feat:` New feature or data source
- `fix:` Bug fix
- `docs:` Documentation update
- `style:` Formatting changes
- `refactor:` Code refactoring

### 5. Push and Create a Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub and fill in the PR template.

## Data Source Standards

### Acceptable Data Sources

✅ **Official Meteorological Agencies**: WMO member organizations, national meteorological services, etc.
✅ **Research Institutions**: Open data from universities and research institutes
✅ **Government Open Data**: Free meteorological data published by governments
✅ **International Organizations**: Data from the United Nations, World Bank, etc.
✅ **Community Projects**: Well-maintained open-source meteorological projects

### Unacceptable Data Sources

❌ **Commercial Data**: Data requiring paid subscriptions
❌ **Restricted Data**: Data with strict usage limitations
❌ **Personal Blogs**: Unofficial, unverified data sources
❌ **Infringing Content**: Data that violates copyrights or agreements

### Data Quality Requirements

- **Accessibility**: Stable links, no special permissions required
- **Timeliness**: Data is updated regularly
- **Completeness**: Metadata and documentation are provided
- **Accuracy**: Data sources are reliable and accurate

## Documentation Standards

### Markdown Format

- Use standard Markdown syntax
- Use `<details>` tags to create collapsible cards
- Use descriptive text for links `🔗 [Description](URL)`
- Add alt text for images `![Description](image-url)`
- Use shields.io badges to display metadata

### Badge Format

All data source entries should use badges to display key information:

```markdown
![Label](https://img.shields.io/badge/Label-Value-Color?style=flat-square)
```

**Color Meanings:**
- `blue` - Basic information such as spatial resolution
- `green` - Time information such as range, time resolution
- `orange` - Update frequency, time range, etc.
- Custom colors - Data source identifiers

### Data Card Structure

Each data source should include the following structure:

```markdown
<details>
<summary><b>Data Name</b> · Brief description</summary>

<!-- Optional: Important notice -->
***Important Notice (if any)***

---

**Sub-type Name** · Optional description

![Badge 1](...)
![Badge 2](...)
![Badge 3](...)
![Source](...)

🔗 [Link Name](URL) · 📅 Data Period · 📝 [Example](./path) · ⚠️ Notes

---

**Another Sub-type**

...

</details>
```

### Link Icon Guide

| Icon | Meaning | Example |
|------|---------|---------|
| 🔗 | Data link | 🔗 [GFS_NOAA](https://...) |
| 📅 | Data period | 📅 Last 10 days |
| 📝 | Example code/documentation | 📝 [Python Example](./sources/example.py) |
| ⚠️ | Notice/Caution | ⚠️ Login required |
| 🔄 | Data status | 🔄 Near real-time |
| 🪜 | Special network needed | 🪜 VPN required |
| 🔍 | Search tip | 🔍 Search keywords |

### Data Field Requirements

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| Data Name | Yes | Name of the data product or service | GFS Global Forecast System |
| Institution | Yes | Data providing institution (in summary) | NOAA/NCEP |
| Resolution | Yes | Spatial resolution (badge) | 0.25° |
| Time Info | Yes | Range or time resolution (badge) | 0~384h(3h) |
| Update Frequency | Yes | Data update frequency (badge) | 4x daily |
| Source | Yes | Data provider (badge) | NOAA |
| Link | Yes | Data access link | [NOMADS](https://...) |
| Data Period | Recommended | Historical data coverage range | 📅 2021 to present |

## Code Standards

### Python Code

```python
# Use descriptive variable names
data_url = "https://example.com/data"
max_retry_attempts = 3

# Add type hints
def download_data(url: str, timeout: int = 30) -> bytes:
    """Download data function description
    
    Args:
        url: Data download link
        timeout: Timeout in seconds
    
    Returns:
        Downloaded binary data
        
    Raises:
        ConnectionError: Raised when connection fails
    """
    pass
```

### Shell Scripts

```bash
#!/bin/bash

# Script description
# Usage: ./script.sh <arguments>

set -euo pipefail  # Strict mode

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
```

## Review Process

### Pull Request Checklist

Before submitting a PR, please confirm:

- [ ] Code/documentation follows project standards
- [ ] All links are valid and accessible
- [ ] Data sources use collapsible card format (`<details>`)
- [ ] All required badges are included (Resolution, Range, Update, Source)
- [ ] Source badge uses the correct color code
- [ ] Necessary tests have been added (if applicable)
- [ ] Related documentation has been updated
- [ ] Commit messages are clear and descriptive
- [ ] Branch has no conflicts with the main branch

### Review Criteria

1. **Functionality**: What problem does the contribution solve
2. **Quality**: Whether code/documentation quality meets standards
3. **Testing**: Whether appropriate test cases are included
4. **Documentation**: Whether related documentation has been updated
5. **Compatibility**: Whether it is compatible with existing content

## Community

### Discussion Channels

- 💬 **GitHub Discussions**: For feature discussions and questions
- 🐛 **GitHub Issues**: For reporting issues and suggesting features
- 📧 **Mailing List**: For important announcements and discussions

### Getting Help

If you encounter difficulties during the contribution process:

1. First, check the documentation and existing Issues
2. Ask questions in Discussions
3. Contact the maintainers

### Becoming a Maintainer

Long-term active contributors can apply to become project maintainers. Responsibilities include:

- Reviewing and merging Pull Requests
- Managing Issues and Discussions
- Mentoring new contributors
- Guiding the project's development direction

---

Thank you for reading this contributing guide! We look forward to your contributions to build a better meteorological data resource community together. 🎉

If you have any questions, please feel free to contact us via [Issues](../../issues).
