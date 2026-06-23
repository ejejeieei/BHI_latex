from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUT_DIR = Path("figures")
OUT_DIR.mkdir(exist_ok=True)


beta = np.round(np.arange(0.0, 2.01, 0.1), 1)

acc_beta_14004 = np.array(
    [
        0.387566137566137,
        0.3855820105820106,
        0.3855820105820106,
        0.3994708994708995,
        0.4751984126984127,
        0.6091269841269842,
        0.7261904761904762,
        0.7619047619047619,
        0.7827380952380952,
        0.7837301587301586,
        0.7863756613756614,
        0.7820767195767195,
        0.7810846560846562,
        0.7880291005291006,
        0.7890211640211641,
        0.8022486772486772,
        0.7797619047619047,
        0.5006613756613756,
        0.5006613756613756,
        0.5006613756613756,
        0.5006613756613756,
    ]
)
std_beta_14004 = np.array(
    [
        0.13642786862695042,
        0.14193867493238405,
        0.14206343048287712,
        0.13120599672822672,
        0.07127684502653198,
        0.0880648453221117,
        0.09789812025832458,
        0.096163657270259,
        0.10614615773885124,
        0.11173823870282805,
        0.1052408501026683,
        0.10853716667800255,
        0.10730909273971007,
        0.1023007270136213,
        0.10266246178015094,
        0.0935922510799965,
        0.10547645920636518,
        0.0270153945310848,
        0.0270153945310848,
        0.0270153945310848,
        0.0270153945310848,
    ]
)

acc_beta_15001 = np.array(
    [
        0.41964285714285715,
        0.4291666666666667,
        0.4642857142857143,
        0.4922619047619048,
        0.5196428571428572,
        0.5410714285714285,
        0.5803571428571429,
        0.6434523809523809,
        0.6934523809523809,
        0.7303571428571428,
        0.7297619047619047,
        0.7148809523809524,
        0.7041666666666666,
        0.6904761904761906,
        0.6613095238095238,
        0.6416666666666667,
        0.6339285714285715,
        0.6273809523809524,
        0.625,
        0.6267857142857144,
        0.6696428571428571,
    ]
)
std_beta_15001 = np.array(
    [
        0.13615607915607905,
        0.10385668162164781,
        0.07342449497671083,
        0.05179255565099753,
        0.0363192805002304,
        0.04845618330698646,
        0.07632753668986612,
        0.11745813892231126,
        0.13802723079128007,
        0.13568687066458676,
        0.13617819624957164,
        0.14355360980793513,
        0.14019721087278425,
        0.12868161063687297,
        0.12196862863819567,
        0.11930329686974678,
        0.11000637736615314,
        0.10765091184407904,
        0.10708331678974964,
        0.11365619029263974,
        0.12731278772522167,
    ]
)

acc_14004 = np.array(
    [
        [0.875, 0.571, 0.696, 0.714, 0.821, 0.571, 0.732, 0.607, 0.732],
        [0.631, 0.560, 0.643, 0.452, 0.655, 0.583, 0.548, 0.512, 0.607],
        [0.562, 0.518, 0.652, 0.509, 0.652, 0.598, 0.589, 0.643, 0.607],
        [0.938, 0.929, 0.857, 0.991, 0.893, 0.929, 0.911, 0.911, 0.902],
        [0.786, 0.562, 0.804, 0.616, 0.866, 0.643, 0.786, 0.679, 0.830],
        [0.821, 0.768, 0.705, 0.714, 0.795, 0.830, 0.759, 0.759, 0.821],
        [0.652, 0.607, 0.661, 0.723, 0.661, 0.688, 0.830, 0.759, 0.705],
        [0.795, 0.696, 0.866, 0.839, 0.848, 0.777, 0.830, 0.893, 0.875],
        [0.804, 0.848, 0.848, 0.812, 0.893, 0.759, 0.804, 0.848, 0.911],
    ]
)

loss_14004 = np.array(
    [
        [0.320, 0.681, 0.563, 0.777, 0.420, 1.944, 0.544, 1.482, 0.558],
        [1.062, 0.683, 0.612, 2.136, 0.672, 1.536, 0.782, 1.622, 0.729],
        [1.856, 0.679, 0.684, 1.928, 0.714, 1.875, 0.738, 1.234, 0.914],
        [0.168, 0.601, 0.281, 0.073, 0.215, 0.202, 0.222, 0.291, 0.193],
        [0.792, 0.679, 0.454, 1.449, 0.329, 1.719, 0.422, 1.087, 0.478],
        [0.627, 0.667, 0.557, 0.825, 0.432, 0.533, 0.469, 0.583, 0.396],
        [1.276, 0.660, 0.701, 0.830, 0.757, 1.092, 0.409, 0.765, 0.865],
        [0.924, 0.609, 0.356, 0.736, 0.315, 1.172, 0.348, 0.483, 0.451],
        [0.750, 0.615, 0.300, 0.847, 0.240, 1.026, 0.434, 0.449, 0.220],
    ]
)

acc_15001 = np.array(
    [
        [0.971, 0.964, 0.971, 0.921, 0.936, 0.636, 0.771, 0.379, 0.771, 0.879, 0.493, 0.243],
        [0.814, 0.964, 0.914, 0.914, 0.879, 0.779, 0.721, 0.500, 0.929, 0.764, 0.707, 0.250],
        [0.779, 0.850, 0.936, 0.771, 0.836, 0.750, 0.743, 0.486, 0.879, 0.671, 0.521, 0.321],
        [0.636, 0.814, 0.714, 0.857, 0.707, 0.521, 0.650, 0.507, 0.814, 0.707, 0.679, 0.507],
        [0.671, 0.757, 0.850, 0.650, 0.893, 0.807, 0.771, 0.457, 0.814, 0.671, 0.536, 0.207],
        [0.600, 0.636, 0.614, 0.586, 0.600, 0.814, 0.521, 0.507, 0.571, 0.600, 0.471, 0.471],
        [0.671, 0.779, 0.771, 0.743, 0.750, 0.550, 0.879, 0.429, 0.679, 0.700, 0.700, 0.386],
        [0.557, 0.579, 0.586, 0.557, 0.586, 0.564, 0.507, 0.543, 0.607, 0.557, 0.564, 0.493],
        [0.600, 0.743, 0.779, 0.643, 0.736, 0.636, 0.664, 0.536, 0.857, 0.607, 0.529, 0.421],
        [0.579, 0.621, 0.671, 0.629, 0.686, 0.614, 0.671, 0.450, 0.671, 0.714, 0.579, 0.450],
        [0.514, 0.586, 0.593, 0.579, 0.593, 0.479, 0.514, 0.521, 0.550, 0.500, 0.714, 0.464],
        [0.464, 0.479, 0.514, 0.507, 0.493, 0.521, 0.493, 0.471, 0.479, 0.529, 0.521, 0.593],
    ]
)

loss_15001 = np.array(
    [
        [0.133, 0.095, 0.125, 0.229, 0.201, 1.711, 0.484, 0.994, 0.756, 0.413, 1.289, 1.524],
        [0.353, 0.119, 0.313, 0.196, 0.322, 0.706, 0.692, 0.972, 0.194, 0.491, 0.760, 1.159],
        [0.447, 0.417, 0.174, 0.543, 0.558, 0.804, 0.565, 1.114, 0.296, 0.622, 1.649, 1.053],
        [0.897, 0.549, 1.158, 0.439, 0.904, 2.193, 0.861, 0.832, 0.532, 0.588, 0.851, 0.772],
        [0.664, 0.625, 0.565, 0.908, 0.344, 0.745, 0.567, 1.083, 0.435, 0.601, 1.355, 1.302],
        [1.046, 0.990, 1.559, 0.978, 1.503, 0.828, 1.377, 0.824, 1.088, 0.681, 1.405, 0.969],
        [0.754, 0.560, 0.814, 0.661, 0.869, 1.791, 0.367, 0.974, 0.661, 0.567, 0.892, 0.972],
        [1.201, 1.107, 1.111, 1.201, 1.538, 1.914, 1.460, 0.791, 0.934, 0.733, 1.198, 0.809],
        [0.904, 0.792, 0.735, 0.961, 0.868, 1.476, 0.751, 0.831, 0.369, 0.665, 1.325, 1.006],
        [1.095, 1.203, 1.081, 0.911, 1.083, 1.502, 0.770, 0.895, 0.691, 0.630, 1.288, 0.839],
        [1.033, 1.151, 1.634, 1.078, 1.729, 2.254, 1.569, 0.963, 1.215, 0.736, 0.899, 0.913],
        [1.280, 1.496, 2.068, 1.348, 1.992, 2.045, 1.703, 0.856, 1.421, 0.778, 1.307, 0.729],
    ]
)


def plot_beta_sweep() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), sharey=True, constrained_layout=True)
    specs = [
        ("BNCI2014004", acc_beta_14004, std_beta_14004, "#1f77b4"),
        ("BNCI2015001", acc_beta_15001, std_beta_15001, "#d62728"),
    ]
    for ax, (title, acc, std, color) in zip(axes, specs):
        best_idx = int(np.argmax(acc))
        best_beta = beta[best_idx]
        best_acc = acc[best_idx]
        ax.plot(beta, acc, color=color, linewidth=2.2, marker="o", markersize=3.5)
        ax.fill_between(beta, acc - std, acc + std, color=color, alpha=0.18)
        ax.axvline(1.0, color="gray", linestyle="--", linewidth=1.2, label=r"$\beta=1$")
        ax.axvline(best_beta, color=color, linestyle=":", linewidth=1.5, label=f"best $\\beta={best_beta:.1f}$")
        ax.scatter([best_beta], [best_acc], color=color, s=35, zorder=3)
        ax.set_title(title, fontsize=11)
        ax.set_xlabel(r"Global scaling factor $\beta$", fontsize=10)
        ax.set_xlim(0.0, 2.0)
        ax.set_ylim(0.35, 0.85)
        ax.grid(alpha=0.25, linewidth=0.6)
        ax.legend(fontsize=8, loc="lower right", frameon=False)
    axes[0].set_ylabel("Average test accuracy", fontsize=10)
    fig.savefig(OUT_DIR / "beta_sweep_curves.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def annotate_heatmap(
    ax,
    data: np.ndarray,
    labels: list[str],
    cmap: str,
    vmin: float,
    vmax: float,
    title: str,
    tick_fontsize: float = 8,
    label_fontsize: float = 9,
    title_fontsize: float = 11,
    text_fontsize: float = 5.8,
    show_values: bool = False,
):
    im = ax.imshow(data, cmap=cmap, vmin=vmin, vmax=vmax, aspect="auto")
    ax.set_title(title, fontsize=title_fontsize)
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=tick_fontsize)
    ax.set_yticklabels(labels, fontsize=tick_fontsize)
    ax.set_xlabel("Source model subject", fontsize=label_fontsize)
    ax.set_ylabel("Test subject", fontsize=label_fontsize)
    if show_values:
        threshold = (vmin + vmax) / 2.0
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                value = data[i, j]
                color = "white" if value > threshold else "black"
                ax.text(j, i, f"{value:.3f}", ha="center", va="center", fontsize=text_fontsize, color=color)
    return im


def plot_cross_subject_compatibility() -> None:
    labels_14004 = [f"S{i}" for i in range(1, 10)]
    labels_15001 = [f"S{i}" for i in range(1, 13)]

    fig, axes = plt.subplots(1, 4, figsize=(20.5, 5.0), constrained_layout=True)
    fig.set_constrained_layout_pads(w_pad=0.01, h_pad=0.01, wspace=0.02, hspace=0.02)

    im1 = annotate_heatmap(
        axes[0],
        acc_14004,
        labels_14004,
        cmap="coolwarm",
        vmin=0.45,
        vmax=1.0,
        title="14004 Acc",
        tick_fontsize=7,
        label_fontsize=8,
        title_fontsize=10,
    )
    fig.colorbar(im1, ax=axes[0], fraction=0.040, pad=0.01)

    im2 = annotate_heatmap(
        axes[1],
        loss_14004,
        labels_14004,
        cmap="YlOrRd",
        vmin=0.07,
        vmax=2.2,
        title="14004 Loss",
        tick_fontsize=7,
        label_fontsize=8,
        title_fontsize=10,
    )
    fig.colorbar(im2, ax=axes[1], fraction=0.040, pad=0.01)

    im3 = annotate_heatmap(
        axes[2],
        acc_15001,
        labels_15001,
        cmap="coolwarm",
        vmin=0.20,
        vmax=1.0,
        title="15001 Acc",
        tick_fontsize=6.5,
        label_fontsize=8,
        title_fontsize=10,
    )
    fig.colorbar(im3, ax=axes[2], fraction=0.040, pad=0.01)

    im4 = annotate_heatmap(
        axes[3],
        loss_15001,
        labels_15001,
        cmap="YlOrRd",
        vmin=0.09,
        vmax=2.3,
        title="15001 Loss",
        tick_fontsize=6.5,
        label_fontsize=8,
        title_fontsize=10,
    )
    fig.colorbar(im4, ax=axes[3], fraction=0.040, pad=0.01)

    fig.savefig(
        OUT_DIR / "cross_subject_compatibility.png",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0.02,
    )
    plt.close(fig)


def main() -> None:
    plot_beta_sweep()
    plot_cross_subject_compatibility()


if __name__ == "__main__":
    main()
