"""init

Revision ID: edace0edb58d
Revises: 
Create Date: 2019-07-16 18:14:27.347041

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'edace0edb58d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Graph_experiment',
    sa.Column('spectra_id', sa.Integer(), nullable=False),
    sa.Column('a', sa.Integer(), nullable=False),
    sa.Column('b', sa.Integer(), nullable=False),
    sa.Column('c', sa.Integer(), nullable=False),
    sa.Column('d', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('spectra_id', name=op.f('pk_Graph_experiment'))
    )
    op.create_table('Spectra_detail',
    sa.Column('spectra_id', sa.Integer(), nullable=False),
    sa.Column('index', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('spectra_id', name=op.f('pk_Spectra_detail')),
    sa.UniqueConstraint('index', name=op.f('uq_Spectra_detail_index'))
    )
    op.create_table('atr',
    sa.Column('atr_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.Column('prism_size_mm', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('number_of_reflections', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('prism_material', sa.Enum('Diamond', 'Ge', 'Si', 'KRS-5', 'ZnS', 'ZnSe', ''), nullable=True),
    sa.Column('angle_of_incidence_degrees', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('spectrometer_ID', mysql.INTEGER(display_width=11), nullable=True),
    sa.PrimaryKeyConstraint('atr_ID', name=op.f('pk_atr')),
    sa.UniqueConstraint('atr_ID', name=op.f('uq_atr_atr_ID'))
    )
    op.create_table('chemical',
    sa.Column('chemical_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.Column('CAS', sa.String(length=45), nullable=True),
    sa.Column('smiles/inchi/mol2', sa.String(length=45), nullable=True),
    sa.Column('chemical formula', sa.String(length=45), nullable=True),
    sa.Column('molecule_ID', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('chemical_ID', name=op.f('pk_chemical')),
    sa.UniqueConstraint('chemical_ID', name=op.f('uq_chemical_chemical_ID'))
    )
    op.create_table('data_aquisition',
    sa.Column('data_aq_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.Column('number_of_sample_scans', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('number_of_background_scans', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('scanner_velocity_KHz', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('resolution', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('start_frequency', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('end_frequency', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('optical_filter', sa.Enum('yes', 'no'), nullable=True),
    sa.Column('higher_range_(cm-1)', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('lower_range_(cm-1)', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('experiment_ID', mysql.INTEGER(display_width=11), nullable=True),
    sa.PrimaryKeyConstraint('data_aq_ID', name=op.f('pk_data_aquisition')),
    sa.UniqueConstraint('data_aq_ID', name=op.f('uq_data_aquisition_data_aq_ID'))
    )
    op.create_table('experiment',
    sa.Column('experiment_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.Column('project_ID', mysql.INTEGER(display_width=6), nullable=True),
    sa.Column('experiment_description', sa.String(length=100), nullable=True),
    sa.Column('related_samples', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('experiment_ID', name=op.f('pk_experiment')),
    sa.UniqueConstraint('experiment_ID', name=op.f('uq_experiment_experiment_ID'))
    )
    op.create_table('experimental_conditions',
    sa.Column('experimental_conditions_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.Column('phase', sa.String(length=45), nullable=True),
    sa.Column('temperature', sa.String(length=45), nullable=True),
    sa.Column('pressure', sa.String(length=45), nullable=True),
    sa.Column('experiment_ID', mysql.INTEGER(display_width=4), nullable=True),
    sa.PrimaryKeyConstraint('experimental_conditions_ID', name=op.f('pk_experimental_conditions')),
    sa.UniqueConstraint('experimental_conditions_ID', name=op.f('uq_experimental_conditions_experimental_conditions_ID'))
    )
    op.create_table('liquid',
    sa.Column('pH', sa.Integer(), nullable=True),
    sa.Column('solvent', sa.String(length=45), nullable=True),
    sa.Column('atmosphere', sa.String(length=45), nullable=True),
    sa.Column('liquid_ID', mysql.INTEGER(display_width=6), autoincrement=True, nullable=False),
    sa.Column('state_of_sample_ID', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('liquid_ID', name=op.f('pk_liquid')),
    sa.UniqueConstraint('liquid_ID', name=op.f('uq_liquid_liquid_ID'))
    )
    op.create_table('molecule',
    sa.Column('molecule_name', sa.String(length=45), nullable=False),
    sa.Column('molecule_ID', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('sample_ID', mysql.INTEGER(display_width=11), nullable=True),
    sa.PrimaryKeyConstraint('molecule_ID', name=op.f('pk_molecule'))
    )
    op.create_table('not_atr',
    sa.Column('not_atr_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.Column('sample_window_material', sa.Enum('CaF2', 'BaF2', 'ZnSe', 'ZnS', 'CdTe', 'KBr', 'KRS-5', 'other', ''), nullable=True),
    sa.Column('pathlength (if known)', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('multi-well_plate', sa.Enum('yes', 'nno', ''), nullable=True),
    sa.Column('product_code', sa.String(length=45), nullable=True),
    sa.Column('spectrometer_ID', mysql.INTEGER(display_width=11), nullable=True),
    sa.PrimaryKeyConstraint('not_atr_ID', name=op.f('pk_not_atr')),
    sa.UniqueConstraint('not_atr_ID', name=op.f('uq_not_atr_not_atr_ID'))
    )
    op.create_table('other',
    sa.Column('other_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('molecule_ID', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('other_ID', name=op.f('pk_other')),
    sa.UniqueConstraint('other_ID', name=op.f('uq_other_other_ID'))
    )
    op.create_table('post_processing_and_deposited_spectra',
    sa.Column('sample_power_spectrum', sa.String(length=45), nullable=True),
    sa.Column('background_power_spectrum', sa.String(length=45), nullable=True),
    sa.Column('initial_result_spectrum', sa.String(length=45), nullable=True),
    sa.Column('initial result spectrum format', sa.Enum('Blackman-Harris 3-Term', '', 'Blackman-Harris 5-Term', 'Norton-Beer,weak', 'Norton-Beer,medium', 'Norton-Beer,strong', 'Boxcar', 'Triangular', 'Four point', 'other'), nullable=True),
    sa.Column('water vapour', sa.String(length=45), nullable=True),
    sa.Column('solvent', sa.String(length=45), nullable=True),
    sa.Column('solution_composition_item_1', sa.String(length=45), nullable=True),
    sa.Column('solution_composition_item_2', sa.String(length=45), nullable=True),
    sa.Column('other', sa.String(length=45), nullable=True),
    sa.Column('baseline_correction', sa.String(length=45), nullable=True),
    sa.Column('scaling', sa.String(length=45), nullable=True),
    sa.Column('2nd_derivative', sa.Enum('yes', 'no', ''), nullable=True),
    sa.Column('method', sa.String(length=45), nullable=True),
    sa.Column('window_point_size/smoothing', sa.String(length=45), nullable=True),
    sa.Column('final_published_spectrum', sa.String(length=45), nullable=True),
    sa.Column('final_published_spectrum_format', sa.Enum('absorbance', 'transmittance', '', 'reflectance', 'log reflectance', 'Kubelka Munk', 'ATR spectrum', 'PAS spectrum'), nullable=True),
    sa.Column('smoothing_method', sa.String(length=45), nullable=True),
    sa.Column('smoothing_parameters', sa.String(length=45), nullable=True),
    sa.Column('spectra_ID', sa.Integer(), nullable=True),
    sa.Column('PPandD_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('PPandD_ID', name=op.f('pk_post_processing_and_deposited_spectra')),
    sa.UniqueConstraint('PPandD_ID', name=op.f('uq_post_processing_and_deposited_spectra_PPandD_ID'))
    )
    op.create_index(op.f('ix_post_processing_and_deposited_spectra_spectra_ID'), 'post_processing_and_deposited_spectra', ['spectra_ID'], unique=False)
    op.create_table('project',
    sa.Column('descriptive_name', sa.String(length=300), nullable=True),
    sa.Column('project_ID', mysql.INTEGER(display_width=6), autoincrement=True, nullable=False),
    sa.Column('related_experiments_ID', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('project_ID', name=op.f('pk_project')),
    sa.UniqueConstraint('project_ID', name=op.f('uq_project_project_ID'))
    )
    op.create_table('protein',
    sa.Column('sample_ID', sa.Integer(), nullable=True),
    sa.Column('protein_ID', mysql.INTEGER(display_width=6), autoincrement=True, nullable=False),
    sa.Column('protein_common_name', sa.String(length=45), nullable=True),
    sa.Column('alternative_names', sa.String(length=45), nullable=True),
    sa.Column('source_organism', sa.String(length=45), nullable=True),
    sa.Column('uniprot_ID', sa.String(length=45), nullable=True),
    sa.Column('sequence', sa.String(length=45), nullable=True),
    sa.Column('expression_system_or_natural_source', sa.String(length=45), nullable=True),
    sa.Column('expressed_as', sa.String(length=45), nullable=True),
    sa.Column('post_translational_modifications', sa.String(length=100), nullable=True),
    sa.Column('mutation_details', sa.String(length=100), nullable=True),
    sa.Column('expression_tags', sa.String(length=100), nullable=True),
    sa.Column('isotopically_labelled', sa.Enum('yes', 'no', ''), nullable=True),
    sa.Column('description_of_labels', sa.String(length=100), nullable=True),
    sa.Column('ligands_present', sa.Enum('yes', 'no', ''), nullable=True),
    sa.Column('molecule_ID', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('protein_ID', name=op.f('pk_protein')),
    sa.UniqueConstraint('protein_ID', name=op.f('uq_protein_protein_ID'))
    )
    op.create_table('publication',
    sa.Column('publication_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.Column('experiment_ID', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('publication_name', sa.String(length=45), nullable=False),
    sa.Column('author', sa.String(length=100), nullable=False),
    sa.Column('link', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('publication_ID', name=op.f('pk_publication')),
    sa.UniqueConstraint('publication_ID', name=op.f('uq_publication_publication_ID'))
    )
    op.create_table('sample',
    sa.Column('sample_ID', mysql.INTEGER(display_width=6), autoincrement=True, nullable=False),
    sa.Column('descriptive_name', sa.String(length=45), nullable=True),
    sa.Column('composition', sa.String(length=45), nullable=True),
    sa.Column('project_ID', mysql.INTEGER(display_width=6), nullable=True),
    sa.PrimaryKeyConstraint('sample_ID', name=op.f('pk_sample')),
    sa.UniqueConstraint('sample_ID', name=op.f('uq_sample_sample_ID'))
    )
    op.create_table('spectra',
    sa.Column('spectra_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.Column('spectra_type', sa.Enum('sample power', 'background power spectrum', 'initial result spectrum', ''), nullable=True),
    sa.Column('format', sa.Enum('absorbance', 'transmittance', 'reflectance', 'log reflectance', 'kubelka munk', 'ATR spectrum', 'pas spectrum', ''), nullable=True),
    sa.Column('experiment_ID', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('spectra_ID', name=op.f('pk_spectra')),
    sa.UniqueConstraint('spectra_ID', name=op.f('uq_spectra_spectra_ID'))
    )
    op.create_table('spectrometer',
    sa.Column('spectrometer_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.Column('instrument_manufacturer', sa.String(length=45), nullable=True),
    sa.Column('instrument_model', sa.String(length=45), nullable=True),
    sa.Column('light_source', sa.Enum('globar', 'laser', 'synchrotron', 'other', ''), nullable=True),
    sa.Column('beamsplitter', sa.Enum('KBr', 'Mylar', ''), nullable=True),
    sa.Column('detector_ type', sa.Enum('DTGS', 'MCT Broad band', 'MCT narrow band', 'other', ''), nullable=True),
    sa.Column('optics', sa.Enum('vacuum', 'purged', 'dry', 'atmospheric', ''), nullable=True),
    sa.Column('type_of_recording', sa.Enum('fourier transform', 'dispersive', 'tunable laser', ''), nullable=True),
    sa.Column('mode_of_recording', sa.Enum('transmission', 'ATR', 'transflectance', 'diffuse reflection', ''), nullable=True),
    sa.Column('experiment_ID', mysql.INTEGER(display_width=11), nullable=True),
    sa.PrimaryKeyConstraint('spectrometer_ID', name=op.f('pk_spectrometer')),
    sa.UniqueConstraint('spectrometer_ID', name=op.f('uq_spectrometer_spectrometer_ID'))
    )
    op.create_table('transf_diffuse',
    sa.Column('trans_diff_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.Column('reflectance_device', sa.String(length=45), nullable=True),
    sa.Column('slide_material', sa.String(length=45), nullable=True),
    sa.Column('angle_of_incidence', sa.String(length=45), nullable=True),
    sa.Column('spectrometer_ID', mysql.INTEGER(display_width=11), nullable=True),
    sa.PrimaryKeyConstraint('trans_diff_ID', name=op.f('pk_transf_diffuse')),
    sa.UniqueConstraint('trans_diff_ID', name=op.f('uq_transf_diffuse_trans_diff_ID'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('role', sa.Text(), nullable=False),
    sa.Column('institution', sa.String(length=45), nullable=True),
    sa.Column('country', sa.String(length=45), nullable=True),
    sa.Column('principle_investigator', sa.String(length=45), nullable=True),
    sa.Column('password_hash', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('name', name=op.f('uq_users_name'))
    )
    op.create_table('FTIRModel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('data', sa.Text(), nullable=False),
    sa.Column('magic', sa.Text(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], name=op.f('fk_FTIRModel_creator_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_FTIRModel')),
    sa.UniqueConstraint('name', name=op.f('uq_FTIRModel_name'))
    )
    op.create_table('exp_has_publication',
    sa.Column('publication_ID', mysql.INTEGER(display_width=4), nullable=False),
    sa.Column('experiment_ID', mysql.INTEGER(display_width=4), nullable=False),
    sa.ForeignKeyConstraint(['experiment_ID'], ['experiment.experiment_ID'], name=op.f('fk_exp_has_publication_experiment_ID_experiment')),
    sa.ForeignKeyConstraint(['publication_ID'], ['publication.publication_ID'], name=op.f('fk_exp_has_publication_publication_ID_publication'))
    )
    op.create_index(op.f('ix_exp_has_publication_experiment_ID'), 'exp_has_publication', ['experiment_ID'], unique=False)
    op.create_index(op.f('ix_exp_has_publication_publication_ID'), 'exp_has_publication', ['publication_ID'], unique=False)
    op.create_table('ft_processing',
    sa.Column('ft_processing_ID', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('apodization_ function', sa.Enum('Blackman-Harris 3-Term', '', 'Blackman-Harris 5-Term', 'Norton-Beer,weak', 'Norton-Beer,medium', 'Norton-Beer,strong', 'Boxcar', 'Triangular', 'Four point', 'other'), nullable=True),
    sa.Column('zero_filling_factor', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('non_linearity_correction', sa.Enum('yes', 'no', ''), nullable=True),
    sa.Column('phase_correction_mode', sa.Enum('Mertz', 'Mertz signed', 'Power spectrum', 'Mertz no peak search', 'Mertz signed no peak search', 'Power spectrum no peak search', ''), nullable=True),
    sa.Column('phase_resolution', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('experiment_ID', mysql.INTEGER(display_width=4), nullable=True),
    sa.ForeignKeyConstraint(['experiment_ID'], ['experiment.experiment_ID'], name=op.f('fk_ft_processing_experiment_ID_experiment')),
    sa.PrimaryKeyConstraint('ft_processing_ID', name=op.f('pk_ft_processing'))
    )
    op.create_table('molecules_in_sample',
    sa.Column('molecular_composition_ID', mysql.INTEGER(display_width=4), autoincrement=True, nullable=False),
    sa.Column('descriptive_name', sa.String(length=45), nullable=True),
    sa.Column('molecule_1_name', sa.String(length=45), nullable=True),
    sa.Column('concentration_1', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('molecule_2_name', sa.String(length=45), nullable=True),
    sa.Column('concentration_2', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('molecule_3_name', sa.String(length=45), nullable=True),
    sa.Column('concentration_3', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('molecule_4_name', sa.String(length=45), nullable=True),
    sa.Column('concentration_4', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('sample_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sample_ID'], ['sample.sample_ID'], name=op.f('fk_molecules_in_sample_sample_ID_sample')),
    sa.PrimaryKeyConstraint('molecular_composition_ID', name=op.f('pk_molecules_in_sample')),
    sa.UniqueConstraint('molecular_composition_ID', name=op.f('uq_molecules_in_sample_molecular_composition_ID'))
    )
    op.create_table('project_has_experiment',
    sa.Column('project_ID', mysql.INTEGER(display_width=6), nullable=True),
    sa.Column('experiment_ID', mysql.INTEGER(display_width=4), nullable=False),
    sa.ForeignKeyConstraint(['experiment_ID'], ['experiment.experiment_ID'], name=op.f('fk_project_has_experiment_experiment_ID_experiment')),
    sa.ForeignKeyConstraint(['project_ID'], ['project.project_ID'], name=op.f('fk_project_has_experiment_project_ID_project')),
    sa.PrimaryKeyConstraint('experiment_ID', name=op.f('pk_project_has_experiment'))
    )
    op.create_index(op.f('ix_project_has_experiment_project_ID'), 'project_has_experiment', ['project_ID'], unique=False)
    op.create_table('state_of_sample',
    sa.Column('state_of_sample_ID', mysql.INTEGER(display_width=6), autoincrement=True, nullable=False),
    sa.Column('state', sa.Enum('gas', 'solid', 'dried film', 'liquid', ''), nullable=False),
    sa.Column('temperature_degrees', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('pressure_PSI', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('sample_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sample_ID'], ['sample.sample_ID'], name=op.f('fk_state_of_sample_sample_ID_sample')),
    sa.PrimaryKeyConstraint('state_of_sample_ID', name=op.f('pk_state_of_sample')),
    sa.UniqueConstraint('state_of_sample_ID', name=op.f('uq_state_of_sample_state_of_sample_ID'))
    )
    op.create_table('association_molecule',
    sa.Column('mols_in_sample_ID', mysql.INTEGER(display_width=4), nullable=False),
    sa.Column('molecule_ID', mysql.INTEGER(display_width=11), nullable=False),
    sa.ForeignKeyConstraint(['molecule_ID'], ['molecule.molecule_ID'], name=op.f('fk_association_molecule_molecule_ID_molecule')),
    sa.ForeignKeyConstraint(['mols_in_sample_ID'], ['molecules_in_sample.molecular_composition_ID'], name=op.f('fk_association_molecule_mols_in_sample_ID_molecules_in_sample')),
    sa.PrimaryKeyConstraint('mols_in_sample_ID', name=op.f('pk_association_molecule'))
    )
    op.create_index(op.f('ix_association_molecule_molecule_ID'), 'association_molecule', ['molecule_ID'], unique=False)
    op.create_table('dried_film',
    sa.Column('atmosphere', sa.String(length=45), nullable=True),
    sa.Column('volume', sa.String(length=45), nullable=True),
    sa.Column('area', sa.String(length=45), nullable=True),
    sa.Column('solvent', sa.String(length=45), nullable=True),
    sa.Column('pH', sa.String(length=45), server_default=sa.text("'RANGE(0,14)'"), nullable=True),
    sa.Column('dried_film_ID', mysql.INTEGER(display_width=6), autoincrement=True, nullable=False),
    sa.Column('state_of_sample_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['state_of_sample_ID'], ['state_of_sample.state_of_sample_ID'], name=op.f('fk_dried_film_state_of_sample_ID_state_of_sample')),
    sa.PrimaryKeyConstraint('dried_film_ID', name=op.f('pk_dried_film')),
    sa.UniqueConstraint('dried_film_ID', name=op.f('uq_dried_film_dried_film_ID'))
    )
    op.create_table('gas',
    sa.Column('atmosphere', sa.String(length=45), nullable=True),
    sa.Column('water_vapour', sa.String(length=45), nullable=True),
    sa.Column('gasID', mysql.INTEGER(display_width=6), autoincrement=True, nullable=False),
    sa.Column('state_of_sample_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['state_of_sample_ID'], ['state_of_sample.state_of_sample_ID'], name=op.f('fk_gas_state_of_sample_ID_state_of_sample')),
    sa.PrimaryKeyConstraint('gasID', name=op.f('pk_gas')),
    sa.UniqueConstraint('gasID', name=op.f('uq_gas_gasID'))
    )
    op.create_table('solid',
    sa.Column('crystal_form', sa.String(length=45), nullable=True),
    sa.Column('chemical_formula', sa.String(length=45), nullable=True),
    sa.Column('solid_ID', mysql.INTEGER(display_width=6), autoincrement=True, nullable=False),
    sa.Column('state_of_sample_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['state_of_sample_ID'], ['state_of_sample.state_of_sample_ID'], name=op.f('fk_solid_state_of_sample_ID_state_of_sample')),
    sa.PrimaryKeyConstraint('solid_ID', name=op.f('pk_solid')),
    sa.UniqueConstraint('solid_ID', name=op.f('uq_solid_solid_ID'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('solid')
    op.drop_table('gas')
    op.drop_table('dried_film')
    op.drop_index(op.f('ix_association_molecule_molecule_ID'), table_name='association_molecule')
    op.drop_table('association_molecule')
    op.drop_table('state_of_sample')
    op.drop_index(op.f('ix_project_has_experiment_project_ID'), table_name='project_has_experiment')
    op.drop_table('project_has_experiment')
    op.drop_table('molecules_in_sample')
    op.drop_table('ft_processing')
    op.drop_index(op.f('ix_exp_has_publication_publication_ID'), table_name='exp_has_publication')
    op.drop_index(op.f('ix_exp_has_publication_experiment_ID'), table_name='exp_has_publication')
    op.drop_table('exp_has_publication')
    op.drop_table('FTIRModel')
    op.drop_table('users')
    op.drop_table('transf_diffuse')
    op.drop_table('spectrometer')
    op.drop_table('spectra')
    op.drop_table('sample')
    op.drop_table('publication')
    op.drop_table('protein')
    op.drop_table('project')
    op.drop_index(op.f('ix_post_processing_and_deposited_spectra_spectra_ID'), table_name='post_processing_and_deposited_spectra')
    op.drop_table('post_processing_and_deposited_spectra')
    op.drop_table('other')
    op.drop_table('not_atr')
    op.drop_table('molecule')
    op.drop_table('liquid')
    op.drop_table('experimental_conditions')
    op.drop_table('experiment')
    op.drop_table('data_aquisition')
    op.drop_table('chemical')
    op.drop_table('atr')
    op.drop_table('Spectra_detail')
    op.drop_table('Graph_experiment')
    # ### end Alembic commands ###
