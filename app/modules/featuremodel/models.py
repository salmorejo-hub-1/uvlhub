from app import db
from sqlalchemy import Enum as SQLAlchemyEnum

from app.modules.dataset.models import Author, PublicationType


class FeatureModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_set_id = db.Column(db.Integer, db.ForeignKey('data_set.id'), nullable=False)
    fm_meta_data_id = db.Column(db.Integer, db.ForeignKey('fm_meta_data.id'))
    files = db.relationship('Hubfile', backref='feature_model', lazy=True, cascade="all, delete")
    fm_meta_data = db.relationship('FMMetaData', uselist=False, backref='feature_model', cascade="all, delete")

    def __repr__(self):
        return f'FeatureModel<{self.id}>'

    def get_cleaned_publication_type(self):
        return self.fm_meta_data.publication_type.name.replace('_', ' ').title()

    def get_total_files_size(self):
        return sum(f.size for f in self.files)

    def get_publication_date(self):
        from app.modules.dataset.repositories import DataSetRepository
        return DataSetRepository().get_by_id(self.data_set_id).created_at

    def to_dict(self):
        return {
            'title': self.fm_meta_data.title,
            'publication_type': self.get_cleaned_publication_type(),
            'description': self.fm_meta_data.description,
            'authors': [author.to_dict() for author in self.fm_meta_data.authors],
            'tags': self.fm_meta_data.tags.split(",") if self.fm_meta_data.tags else [],
            'id': self.id,
            'files': [file.to_dict() for file in self.files],
            'publication_date': self.get_publication_date(),

        }


class FMMetaData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uvl_filename = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    publication_type = db.Column(SQLAlchemyEnum(PublicationType), nullable=False)
    publication_doi = db.Column(db.String(120))
    tags = db.Column(db.String(120))
    uvl_version = db.Column(db.String(120))
    fm_metrics_id = db.Column(db.Integer, db.ForeignKey('fm_metrics.id'))
    fm_metrics = db.relationship('FMMetrics', uselist=False, backref='fm_meta_data')
    authors = db.relationship('Author', backref='fm_metadata', lazy=True, cascade="all, delete",
                              foreign_keys=[Author.fm_meta_data_id])

    def __repr__(self):
        return f'FMMetaData<{self.title}'


class FMMetrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solver = db.Column(db.Text)
    not_solver = db.Column(db.Text)

    def __repr__(self):
        return f'FMMetrics<solver={self.solver}, not_solver={self.not_solver}>'
