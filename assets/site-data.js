window.EuclidSiteData = {
  euclidQuasars: window.EuclidPublishedSample || [],
  comparisonSample: window.EuclidComparisonSample || [],
  skyMapOverlays: window.EuclidSkyMapOverlays || null,
  papers: [
    {
      id: "paper-barnett-2019",
      title: "Euclid preparation. V. Predicted yield of redshift 7 < z < 9 quasars from the wide survey",
      year: 2019,
      publishedDate: "2019-10-21",
      authors: "R. Barnett, S. J. Warren, D. J. Mortlock et al.",
      venue: "A&A",
      description:
        "Forecasts the number of quasars that the Euclid wide survey should uncover at 7 < z < 9, emphasizing the value of complementary z-band imaging for selection.",
      tags: ["sample", "selection"],
      adsUrl: "https://ui.adsabs.harvard.edu/abs/2019A%26A...631A..85E/abstract",
      relatedQuasarIds: []
    },
    {
      id: "paper-yang-2026",
      title: "Euclid: Discovery of 31 new quasars at 6.6 < z < 7.8",
      year: 2026,
      publishedDate: "2026-07-06",
      authors: "D. Yang, J. Hennawi, F. Guarneri et al.",
      venue: "A&A",
      description:
        "First results from the Euclid wide survey, presenting 31 new quasars at 6.6 < z < 7.8.",
      tags: ["sample", "selection"],
      adsUrl: "https://www.aanda.org/articles/aa/abs/2026/07/aa58883-26/aa58883-26.html",
      relatedQuasarIds: [
        "J0315-6844",
        "J1732+6016",
        "J1811+6145",
        "J0446-5700",
        "J0916+6836",
        "J0451-3426",
        "J1155+7046",
        "J0443-5332",
        "J1537+5829",
        "J1505+7734",
        "J1434+6857",
        "J0252-4125",
        "J1543+4718",
        "J1707+6502",
        "J0250-5317",
        "J0502-3849",
        "J0526-4609",
        "J1555+5152",
        "J0933+7427",
        "J1614+4528",
        "J1722+5741",
        "J1340+6747",
        "J0412-5639",
        "J1631+6259",
        "J1418+6949",
        "J1445+7143",
        "J1355+7000",
        "J0522-5127",
        "J1012+6630",
        "J1253+7054",
        "J1729+6410"
      ]
    },
    {
      id: "paper-belladitta-2026",
      title: "Euclid: A UV-faint quasar in a highly luminous star-forming host galaxy at z ≈ 7.7",
      year: 2026,
      publishedDate: "2026-07-06",
      authors: "S. Belladitta, R. Decarli, E. Banados et al.",
      venue: "A&A",
      description:
        "NOEMA follow-up observations of a UV-faint quasar in a highly luminous star-forming host galaxy at z ≈ 7.7.",
      tags: ["host galaxy", "submm"],
      adsUrl: "https://arxiv.org/abs/2607.03430",
      relatedQuasarIds: ["J1253+7054"]
    }
  ],
  team: [
    {
      name: "Daming Yang",
      role: "Graduate student",
      affiliation: "Leiden Observatory, Graduate student",
      focus: "High-redshift quasar selection and follow-up.",
      image: "assets/team/daming-yang.jpg"
    },
    {
      name: "Joseph Hennawi",
      role: "Faculty",
      affiliation: "Leiden Observatory / University of California, Santa Barbara, Faculty",
      focus: "Quasar science and survey strategy.",
      image: null
    },
    {
      name: "Jan-Torge Schindler",
      role: "Faculty, current co-lead",
      affiliation: "Hamburg Observatory, Faculty, current co-lead",
      focus: "Quasar selection and survey analysis.",
      image: null
    },
    {
      name: "Francesco Guarneri",
      role: "Postdoc",
      affiliation: "Hamburg Observatory, Postdoc",
      focus: "Catalog work and imaging analysis.",
      image: null
    },
    {
      name: "Eduardo Banados",
      role: "Faculty",
      affiliation: "Max-Planck-Institut für Astronomie, Faculty",
      focus: "High-redshift quasars and follow-up observations.",
      image: null
    },
    {
      name: "Daniel Mortlock",
      role: "Faculty",
      affiliation: "Imperial College London, Faculty",
      focus: "Quasar demographics and survey interpretation.",
      image: null
    },
    {
      name: "Feige Wang",
      role: "Faculty",
      affiliation: "University of Michigan, Faculty",
      focus: "High-redshift quasars and early-universe observations.",
      image: null
    },
    {
      name: "Jinyi Yang",
      role: "Faculty",
      affiliation: "University of Michigan, Faculty",
      focus: "Quasar discovery and follow-up analysis.",
      image: null
    },
    {
      name: "Xiaohui Fan",
      role: "Faculty",
      affiliation: "University of Arizona, Faculty",
      focus: "Quasar surveys and high-redshift quasar populations.",
      image: null
    },
    {
      name: "Silvia Belladitta",
      role: "Postdoc, current co-lead",
      affiliation: "Max-Planck-Institut für Astronomie, Postdoc, current co-lead",
      focus: "Imaging analysis and quasar candidate validation.",
      image: null
    },
    {
      name: "Julien Wolf",
      role: "Postdoc",
      affiliation: "Max-Planck-Institut für Astronomie, Postdoc",
      focus: "Survey analysis and data validation.",
      image: null
    },
    {
      name: "Anna-Christina Eilers",
      role: "Faculty",
      affiliation: "Massachusetts Institute of Technology, Faculty",
      focus: "High-redshift quasars and spectroscopy.",
      image: null
    },
    {
      name: "Daniel Stern",
      role: "Faculty",
      affiliation: "JPL, Faculty",
      focus: "Infrared surveys and quasar follow-up.",
      image: null
    },
    {
      name: "Yoshiki Matsuoka",
      role: "Faculty",
      affiliation: "Ehime University, Faculty",
      focus: "Quasar surveys and public science catalogs.",
      image: null
    },
    {
      name: "Masafusa Onoue",
      role: "Faculty",
      affiliation: "Waseda University, Faculty",
      focus: "High-redshift quasars and survey interpretation.",
      image: null
    },
    {
      name: "Arvind Hughes",
      role: "Postdoc",
      affiliation: "Imperial College London, Postdoc",
      focus: "Quasar survey analysis and follow-up.",
      image: null
    },
    {
      name: "Ben Wang",
      role: "Graduate student",
      affiliation: "Leiden Observatory / Tsinghua University, Graduate student",
      focus: "High-redshift quasar selection and catalog work.",
      image: null
    },
    {
      name: "Chris Willott",
      role: "Faculty",
      affiliation: "Herzberg, Faculty",
      focus: "Quasar surveys and early-universe observations.",
      image: null
    },
    {
      name: "Frederick Davies",
      role: "Faculty",
      affiliation: "Max-Planck-Institut für Astronomie, Faculty",
      focus: "High-redshift quasars and spectroscopy.",
      image: null
    },
    {
      name: "Giustina Vietri",
      role: "Postdoc",
      affiliation: "INAF, Postdoc",
      focus: "Imaging analysis and quasar candidate validation.",
      image: null
    },
    {
      name: "Huub Rottgering",
      role: "Faculty",
      affiliation: "Leiden Observatory, Faculty",
      focus: "Survey science and team coordination.",
      image: null
    },
    {
      name: "Ji-Jia Tang",
      role: "Postdoc",
      affiliation: "Ehime University, Postdoc",
      focus: "Quasar follow-up and public science catalogs.",
      image: null
    },
    {
      name: "Knud Janke",
      role: "Faculty",
      affiliation: "Max-Planck-Institut für Astronomie, Faculty",
      focus: "Survey strategy and quasar science.",
      image: null
    },
    {
      name: "Roberto Decarli",
      role: "Faculty",
      affiliation: "INAF, Faculty",
      focus: "Quasar follow-up observations and interpretation.",
      image: null
    },
    {
      name: "Sarah Bosman",
      role: "Faculty",
      affiliation: "Max-Planck-Institut für Astronomie, Faculty",
      focus: "High-redshift quasars and reionization studies.",
      image: null
    },
    {
      name: "Yuming Fu",
      role: "Postdoc",
      affiliation: "Leiden Observatory, Postdoc",
      focus: null,
      image: null
    },
    {
      name: "Aaron Barth",
      role: "Faculty",
      affiliation: "University of California, Irvine, Faculty",
      focus: null,
      image: null
    }
  ]
};
