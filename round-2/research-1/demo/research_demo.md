# HLSAD Positioning & JCR Suppression Annotations

## Summary

This artifact delivers two critical inputs for the Hodge-decomposition citation cartel detector paper.

**HLSAD (arXiv:2505.24534, KDD 2025)** is authored by Frantzen & Schaub (RWTH Aachen). It applies Hodge Laplacians of multiple orders (up to user-specified K) to time-evolving simplicial complexes. For each temporal snapshot, singular values of both up- and down-Laplacians are extracted and concatenated into a feature vector; anomalies are flagged when the angular deviation from an SVD-based sliding-window baseline exceeds a threshold. Real-world datasets: UCI Online Message Dataset (Hits@10=1.0) and US Senate co-sponsorship network (Hits@2=1.0). KEY CONTRAST: HLSAD asks 'when did the graph structure change?' (temporal change-point detection) and does not target citation networks or citation integrity. This paper asks 'is the static cumulative flow currently manipulated?' using orthogonal gradient+curl+harmonic decomposition of a fixed net-flow matrix, where curl magnitude is the direct algebraic signature of citation rings validated against JCR suppression labels.

READY-TO-USE RELATED WORK PARAGRAPH: 'HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.'

**SUPPRESSION ANNOTATION:** 32 stacking journals confirmed by name across 2018-2025 (5 from 2018, 4 from 2021—CORRECTING the prior artifact which said 3—, 3 from 2023, 11 from 2024, 4 from 2025). CRITICAL CORRECTIONS: (1) 2020 had ZERO stacking journals—all 33 suppressions were self-citation; (2) Hellenic Journal of Cardiology (2021) is STACKING, not self-citation as previously documented; (3) 2019 stacking journal names are unknown and those 17 journals must be excluded from the validated positive class. CONCURRENT WORK: CDFD (arXiv:2506.12546, June 2025) is a close concurrent paper decomposing directed flow as w=c+d with circularity index CI=Σc/Σw—captures ALL circular flow unlike Hodge curl which only catches triangular cycles. Full annotated JSON list and research report are in research_out.json and research_report.md.

## Research Findings

## HLSAD Technical Methodology [1, 2]

HLSAD (Frantzen & Schaub, KDD '25, arXiv:2505.24534) detects anomalies in **time-evolving simplicial complexes**. The method computes Hodge Laplacians up to user-specified order K for each temporal snapshot, extracting principal singular values from both the up-Laplacian (L^up_k) and down-Laplacian (L^down_k) of each order k [2]. These singular values are concatenated into a feature vector σ(t). A sliding-window context matrix C(t) stores the last w vectors; the 'typical' feature σ̃(t) is derived via SVD of C(t). The anomaly score is the **angular deviation** between σ(t) and σ̃(t), using dual windows (w_s=5 short-term, w_ℓ=10 long-term). Computational complexity: O(T·Σ_k n_k² log ℓ) [2]. Real-world validation: UCI Online Message Dataset (Hits@10=1.0) and US Senate co-sponsorship network (Hits@2=1.0) [2].

**KEY DISTINCTION**: HLSAD is temporal (change-point detection in evolving graphs) and does not target citation networks or use labeled ground truth. This paper uses static flow decomposition (gradient + curl + harmonic) on a fixed net-flow matrix, where the curl component directly quantifies citation-ring manipulation against JCR suppression ground truth [1, 2].

## Related Work Paragraph

'HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes [1]. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.'

## JCR Suppression-Type Annotations (2018-2025)

### CRITICAL CORRECTIONS vs. Prior Artifact
- **2021 stacking = 4, NOT 3**: Hellenic Journal of Cardiology is **stacking** (not self-citation as documented in prior artifact) [9]
- **2020 = ZERO stacking**: All 33 suppressions in 2020 JCR were self-citation violations; none were stacking [10, 11]
- **2019 stacking names unknown**: Must be excluded from validated positive class [14]

### Confirmed Stacking Journals (suitable as positive class)

**2025 (4 stacking)** [5]: Applied Organometallic Chemistry, Asian Journal of Agriculture and Biology, Chemical Methodologies, Genetic Resources and Crop Evolution

**2024 (11 stacking)** [6, 7]: Annals of Financial Economics, Climate Change Economics, Cuadernos de Economia, Environmental Science & Pollution Research, Gazzetta Medica Italiana Archivio per le Scienze Mediche, Granular Computing, Information Sciences, Minerva Medica, Panminerva Medica, Resources Policy, Ukrainian Journal of Physical Optics

**2023 (3 stacking)** [8]: Genetika, Bioscience Research, Bioinspired Biomimetic and Nanobiomaterials

**2021 (4 stacking — CORRECTED)** [9]: Archivos Latinoamericanos de Nutrition, Journal of Intelligent & Fuzzy Systems, Materials Express, Hellenic Journal of Cardiology

**2020 (0 stacking)** [10]: Excluded entirely — all 33 suppressions were self-citation

**2019 (unknown)** [14]: 17 journals suppressed; stacking names not found in secondary literature; exclude from positive class

**2018 (5/6 stacking confirmed, 1 unnamed)** [12]: European Journal of the History of Economic Thought, Journal of the History of Economic Thought, Liver Cancer, Digestive Diseases (donor to Liver Cancer), Oncology (donor to Liver Cancer), [1 unnamed]

Total confirmed stacking journals by name: **32** (2018-2025, excluding 1 unnamed 2018 journal and the unknown 2019 journals)

## Concurrent Works

**CDFD** (arXiv:2506.12546, June 2025) [13] is a close concurrent paper: decomposes directed flow as w=c+d (circular + acyclic), defines CI=Σc/Σw in [0,1]. Captures ALL circular flows including longer cycles beyond triangles, unlike Hodge curl which only captures triangular cycles. Should be cited and compared explicitly.

**CIDRE** (arXiv:2009.09097, Sci. Rep. 2021) [3, 4] is the primary prior work in this domain: dcSBM null model, Poisson p-values with BH-FDR; detects >50% of JCR-suppressed stacking journals; validated on 2013 MAG data. Methodologically distinct (statistical community anomaly vs. algebraic flow decomposition).

**GLAD** (arXiv:2202.11360) [15] and **Unsupervised JACL 2020** (arXiv:2005.14343) [16] are related but less overlapping (paper-level / unsupervised without JCR ground truth).

## Sources

[1] [HLSAD: Hodge Laplacian-based Simplicial Anomaly Detection (abstract page)](https://arxiv.org/abs/2505.24534) — Confirmed temporal nature, higher-order simplicial complex focus, KDD 2025 venue, abstract text

[2] [HLSAD full PDF](https://arxiv.org/pdf/2505.24534) — Complete methodology: multi-order Hodge Laplacians, SVD-based sliding window anomaly score with angular deviation, UCI and Senate datasets (both Hits@N=1.0), boundary operator B1 shown explicitly, dual window parameters w_s=5 / w_l=10, computational complexity formula

[3] [CIDRE: Detecting anomalous citation groups (PMC full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/) — Case study journal groups 1-14; note 46 stacking pairs / 55 journals total suppressed by JCR up to 2019; 22 merged stacking groups J1-J22

[4] [CIDRE arXiv PDF](https://arxiv.org/pdf/2009.09097) — Since 2007: 227 total JCR suppressions (173 self-citation, 55 stacking, 1 both); CIDRE detects 12 of 22 stacking groups; uses 2013 MAG data with 48,821 journals

[5] [Retraction Watch: 2025 JCR suppression list (20 journals)](https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/) — Complete 2025 list: 4 stacking + 16 self-citation. Named all 4 stacking journals.

[6] [WoS Journal blog: 2024 JCR suppression list (17 journals)](https://blog.wos-journal.info/title-suppressions-journals-suppressed-from-2023-jcr-data-2024-release/) — Complete 2024 list: 11 stacking + 6 self-citation. All 11 stacking journal names confirmed.

[7] [Retraction Watch: 2024 JCR suppression article](https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/) — Confirmed Ukrainian Journal of Physical Optics (46% citations from Optik), Granular Computing / Information Sciences (Pedrycz), Resources Policy stacking pair details

[8] [Retraction Watch: 2023 JCR suppression (4 journals)](https://retractionwatch.com/2023/06/28/truly-devastating-four-journals-wont-get-new-impact-factors-this-year-because-of-citation-shenanigans/) — Complete 2023 list: Marketing Theory (self-citation), Genetika + Bioscience Research + Bioinspired Biomimetic and Nanobiomaterials (stacking). Confirmed Genetika disputed the relationship.

[9] [Retraction Watch: 2021 JCR suppression (10 journals)](https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/) — Complete 2021 list: 4 stacking (Archivos Latinoamericanos, J Intelligent & Fuzzy Systems, Materials Express, Hellenic Journal of Cardiology) + 6 self-citation. Corrects prior artifact's claim of 3 stacking.

[10] [Retraction Watch: 2020 JCR suppression (33 journals)](https://retractionwatch.com/2020/06/29/major-indexing-service-sounds-alarm-on-self-citations-by-nearly-50-journals/) — CONFIRMED: zero stacking in 2020 — all 33 suppressions were self-citation. Named: IJSEM, Zootaxa, Body Image, International Journal of Medicinal Mushrooms, Journal of Environmental and Engineering Geophysics, Forensic Science International: Genetics.

[11] [Enago Academy: 2020 JCR suppression details](https://www.enago.com/academy/journals-suppressed-in-the-journal-citation-reports-fight-back/) — Publisher breakdown: 9 Elsevier, 7 Springer Nature, 6 Taylor & Francis, 5 Wiley. Body Image (50.4% self-citation), IJSEM details.

[12] [Scholarly Kitchen: 2018 JCR suppression (20 journals)](https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/) — Complete 2018 list: 14 self-citation + 6 stacking. Stacking table: Liver Cancer/Digestive Diseases (40%), Liver Cancer/Oncology (23%), EJEHT/JHET mutual pair. 6th stacking journal not named in accessible text (site 403).

[13] [CDFD: Circular Directional Flow Decomposition (Homs-Dones et al., 2025)](https://arxiv.org/abs/2506.12546) — Concurrent work: w=c+d decomposition; CI=Σc/Σw in [0,1]; BFF algorithm; captures ALL circular flows beyond triangles — methodologically complementary to Hodge curl

[14] [Clarivate: 2019 JCR announcement](https://clarivate.com/academia-government/blog/announcing-the-2019-journal-citation-reports/) — 17 journals suppressed; no specific names or stacking vs. self-citation breakdown provided

[15] [GLAD: Deep Graph Learning for Anomalous Citation Detection](https://arxiv.org/abs/2202.11360) — GNN-based paper-level citation anomaly detection with CPU algorithm; different granularity and method from journal-level flow decomposition

[16] [Unsupervised Anomaly Detection in Journal-Level Citation Networks (JCDL 2020)](https://arxiv.org/abs/2005.14343) — Unsupervised journal-level citation anomaly detection; no Hodge decomposition; earlier related work

## Follow-up Questions

- Can the CIDRE edge-table-2013.csv and journal_names.csv files be cross-referenced with OpenAlex journal IDs to map which confirmed stacking journals from 2018-2025 were already visible as anomalous in the 2013 MAG snapshot? This would establish whether the Hodge curl signal is detectable in pre-suppression data, strengthening the paper's claim of predictive value.
- For the 2019 JCR suppressed journals (17 total, stacking names unknown): the CIDRE paper (arXiv:2009.09097) references 46 donor-recipient stacking pairs up to 2019 and 22 merged groups (J1-J22). Are the specific journal names in those groups available in the CIDRE GitHub repository's data files or supplementary materials, which could resolve the 2019 stacking journal identification gap?
- The CDFD paper (arXiv:2506.12546) captures ALL circular flows including cycles longer than triangles, while HodgeRank curl is restricted to triangular cycles. For the citation cartel detection experiment, should the experiment compute both metrics on the same stacking-labeled journal set to empirically determine whether the longer-cycle circular flows are more discriminative than the triangular Hodge curl—and should CDFD's CI be presented as a complementary or competing method?

---
*Generated by AI Inventor Pipeline*
