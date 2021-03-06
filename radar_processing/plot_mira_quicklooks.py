import os
import gc
import matplotlib.pyplot as plt
import pyart

from read_mira_radar import read_multi_mira


def read_plot_mira_quicklooks(filenames, save_path="figs/", res=5):
    """
    """

    # Reading files
    print("Reading MIRA files")
    mira, mira_melthei = read_multi_mira(
        filenames, for_quicklooks=True, ql_res=res
    )

    # Grabbing date from MIRA file
    date = pyart.util.datetimes_from_radar(mira)[0]

    # Generating x axes for Melting Layer Height data
    # print(mira_melthei[0]['data'])
    # times = pyart.util.datetimes_from_radar(mira)
    # times = times.astype("datetime64[ns]")
    times = []

    # Criando diretório para salvar as figuras
    try:
        os.makedirs(save_path + date.strftime("%Y/%m/%d/"))
    except FileExistsError:
        pass
    save_path = save_path + date.strftime("%Y/%m/%d/")

    # Plotando
    print("Plotting/saving MIRA variables")

    display = pyart.graph.RadarDisplay(mira)

    plot_mira_field(
        field="SNRg",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["SNRg"]["yrange"][0],
        vmax=mira.fields["SNRg"]["yrange"][1],
        cmap="pyart_Carbone17",
        figname=save_path + "mira_snrg_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="SNR",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["SNR"]["yrange"][0],
        vmax=mira.fields["SNR"]["yrange"][1],
        cmap="pyart_Carbone17",
        figname=save_path + "mira_snr_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="Zg",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["Zg"]["yrange"][0],
        vmax=40,
        cmap="pyart_Theodore16",
        figname=save_path + "mira_zg_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="Ze",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["Ze"]["yrange"][0],
        vmax=40,
        cmap="pyart_Theodore16",
        figname=save_path + "mira_ze_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="Z",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["Z"]["yrange"][0],
        vmax=40,
        cmap="pyart_Theodore16",
        figname=save_path + "mira_z_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="RR",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["RR"]["yrange"][0],
        vmax=mira.fields["RR"]["yrange"][1],
        cmap="pyart_RRate11",
        figname=save_path + "mira_rr_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="LWC",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["LWC"]["yrange"][0],
        vmax=mira.fields["LWC"]["yrange"][1],
        cmap=None,
        figname=save_path + "mira_lwc_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="VELg",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["VELg"]["yrange"][0],
        vmax=mira.fields["VELg"]["yrange"][1],
        cmap="pyart_BuDRd18",
        figname=save_path + "mira_velg_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="VEL",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["VEL"]["yrange"][0],
        vmax=mira.fields["VEL"]["yrange"][1],
        cmap="pyart_BuDRd18",
        figname=save_path + "mira_vel_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="LDRg",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["LDRg"]["yrange"][0],
        vmax=mira.fields["LDRg"]["yrange"][1],
        cmap="pyart_SCook18",
        figname=save_path + "mira_ldrg_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="LDR",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["LDR"]["yrange"][0],
        vmax=mira.fields["LDR"]["yrange"][1],
        cmap="pyart_SCook18",
        figname=save_path + "mira_ldr_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="RHO",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["RHO"]["yrange"][0],
        vmax=mira.fields["RHO"]["yrange"][1],
        cmap="pyart_RefDiff",
        figname=save_path + "mira_rho_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="RHOwav",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["RHOwav"]["yrange"][0],
        vmax=mira.fields["RHOwav"]["yrange"][1],
        cmap="pyart_RefDiff",
        figname=save_path + "mira_rhowav_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="DPS",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["DPS"]["yrange"][0],
        vmax=mira.fields["DPS"]["yrange"][1],
        cmap="pyart_Wild25",
        figname=save_path + "mira_dps_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="DPSwav",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["DPSwav"]["yrange"][0],
        vmax=mira.fields["DPSwav"]["yrange"][1],
        cmap="pyart_Wild25",
        figname=save_path + "mira_dpswav_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="RMSg",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["RMSg"]["yrange"][0],
        vmax=mira.fields["RMSg"]["yrange"][1],
        cmap="pyart_NWS_SPW",
        figname=save_path + "mira_rmsg_" + date.strftime("%Y%m%d%H%M%S"),
    )

    plot_mira_field(
        field="RMS",
        times=times,
        melting_height=mira_melthei[0]["data"] / 1000,
        display=display,
        vmin=mira.fields["RMS"]["yrange"][0],
        vmax=mira.fields["RMS"]["yrange"][1],
        cmap="pyart_NWS_SPW",
        figname=save_path + "mira_rms_" + date.strftime("%Y%m%d%H%M%S"),
    )

    del mira, mira_melthei, date, times, display
    gc.collect()


def plot_mira_field(
    field, times, melting_height, display, vmin, vmax, cmap, figname
):
    """
    """

    plt.ioff()

    fig = plt.figure(figsize=(15, 5))  # (10, 5)

    display.plot_vpt(
        field,
        vmin=vmin,
        vmax=vmax,
        cmap=cmap,
        time_axis_flag=True,
        mask_outside=True,
        raster=True,
    )
    # plt.plot(times, melting_height, "k-", label="Melting Layer Height")
    display.plot_grid_lines()
    # plt.legend(loc="upper right")
    plt.ylim((0, 18))

    plt.savefig(figname + ".png", dpi=300, bbox_inches="tight")

    plt.clf()
    plt.close()
    del fig
    gc.collect()
